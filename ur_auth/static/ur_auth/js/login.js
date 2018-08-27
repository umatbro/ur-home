function init() {
  gapi.load('auth2', () => {
      gapi.auth2.init({
           // client_id: '1035712948704-5cr1c68idk5cs6bvv2q9j48bebc7kbr6.apps.googleusercontent.com',
        });
  });
}

document.addEventListener('DOMContentLoaded', () => {


function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}

});
