import requests
import json
from kivy.app import App



class myFirebase():
    vak = "AIzaSyDUhUbIGDbMnvDqISv-ZHT47cTKxTCHTCg"
    def sign_up(self, email, password):
        app = App.get_running_app()
        sign_up_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key= " + self.vak
        sign_up_data = {"email": email, "password": password, "returnSecureToken": True}
        sign_up_request = requests.post(sign_up_url, data = sign_up_data)
        print(sign_up_request.ok)
        print(sign_up_request.content.decode())
        if sign_up_request.ok == True:
            App.get_running_app().root.current = "main"
        if sign_up_request.ok == False:
            error_data = json.loads(sign_up_request.content.decode())
            error_message = error_data["error"]['message']


        pass

    def sign_in_existing_user(self, email, password):
        """Called if a user tried to sign up and their email already existed."""
        signin_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + self.vak
        signin_payload = {"email": email, "password": password, "returnSecureToken": True}
        signin_request = requests.post(signin_url, data=signin_payload)
        sign_up_data = json.loads(signin_request.content.decode())
        app = App.get_running_app()

        if signin_request.ok == True:
            App.get_running_app().root.current = "main"
        elif signin_request.ok == False:
            error_data = json.loads(signin_request.content.decode())
            error_message = error_data["error"]['message']

