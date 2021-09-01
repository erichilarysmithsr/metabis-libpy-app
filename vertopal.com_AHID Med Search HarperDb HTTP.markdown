OkHttpClient client = new OkHttpClient().newBuilder() .build();
MediaType mediaType = MediaType.parse(\"application/json\"); RequestBody
body = RequestBody.create(mediaType, \"{\\n \\\"operation\\\":
\\\"create_schema\\\",\\n \\\"schema\\\": \\\"dev\\\"\\n}\"); Request
request = new Request.Builder()
.url(\"https://app-aphidmedsearch.harperdbcloud.com\") .method(\"POST\",
body) .addHeader(\"Content-Type\", \"application/json\")
.addHeader(\"Authorization\", \"Basic
ZXJpY2hpbGFyeXNtaXRoc3I6b25jYWxsOTEx\") .build(); Response response =
client.newCall(request).execute();
