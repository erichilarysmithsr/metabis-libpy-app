# Pusher Index.py File

import pusher

pusher_client = pusher.Pusher(
  app_id='1496852',
  key='3827e41e96b587fd01b0',
  secret='f9ea2b42a547b7cba96e',
  cluster='mt1',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})
