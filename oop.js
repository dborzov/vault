//superclass method
this._super();

// extending objects right
$.extend(extendable, extendablees)

// what they call "class" in js:
function Account () {
  this._currentBalance = 0;
}
Account.prototype.balance = function () {
  return this._currentBalance;
}
Account.prototype.deposit = function (howMuch) {
  this._currentBalance = this._currentBalance + howMuch;
  return this;
}
var account = new Account();

