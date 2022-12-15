$.get("https://stefanbohacek.com/hellosalut/?lang=fr", function(data) {
  $("div#hello").text(data.hello);
});
