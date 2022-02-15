function copy() {
  let textarea = document.getElementById("convert-text");
  textarea.select();
  document.execCommand("copy");
}