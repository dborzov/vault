var a = "abcdef abcdef";
var r1 = new RegExp("a");
var r2 = new RegExp("a", "g"); // "g" parameter for all occurances
a.replace("a", "A"); //Returns "Abcdef abcdef"
a.replace(r1, "A"); //Returns "Abcdef abcdef"
a.replace(r2, "A"); //Returns "Abcdef Abcdef"