# voiceRecognition.py
It converts Base64encoded voice data to Text.

With this you can convert Base64 encoded audio data to wav and then to speech. 

Input is, Base64 encoded string of audio recorded at 16000Hz with sample size of 2 bytes and duration of audio. 

After this Base64 is converted to wav, Speech recognition converts speech to text.

Base64 string is used to transmit audio data embedded in HTTP request to transmit audio data over server.

