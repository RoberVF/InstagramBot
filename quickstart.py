from instapy import InstaPy
from instapy import smart_run

# Datos de la cuenta
insta_username = ''
insta_password = ''

comments = ['Desde Vadanishop queremos decirte que nos encanta tu mascota',
        'Ohh, maravilloso',
        '¡¡Que guapa se ve la mascota!!',]

# set headless_browser=True #correr en background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):		
  
  # actividad		
  session.follow_by_tags(["perros", "gatos"], amount=20)
#   session.like_by_tags(["perros", "gatos"], amount=20)
  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
#   session.join_pods(topic='sports', engagement_mode='no_comments')