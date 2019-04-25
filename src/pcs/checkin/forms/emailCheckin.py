# Checkin form to register their attendance at a contest

from django import forms
from django.core.exceptions import ValidationError
from registration.models import Account
from registration.utility import auth

class emailCheckinForm(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))

    def validUser(self, req):
        # userExists will check that user is in db
        # if they don't match or are not in the db an error will
        # display and the user will have to try again.
        if auth.userExists(req):
            # mark user at checked in
            user = auth.getUser(req)
            user.isSignedIn = True
            user.save()
            return True

        else:
            return False
            #raise ValidationError(
                #('This email '), code='notexits')