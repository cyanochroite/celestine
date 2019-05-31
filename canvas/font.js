/* JSLint edition 2019-01-31 */
/*jslint
    bitwise:true, browser:true
*/
/*global
    font, int
*/
/*property
    hi, lo
*/
/**
    @param {number} hi
    @param {number} lo
*/
function int(hi, lo) {
    "use strict";
    var out = {};
    out.hi = hi;
    out.lo = lo;
    return out;
}
var font = {
    "0": int(0x38101010, 0x10101000),
    "1": int(0x7C381010, 0x10101000),
    "2": int(0xFE103810, 0x10101000),
    "3": int(0xFE7C3810, 0x10101000),
    "4": int(0x38101010, 0x38383800),
    "5": int(0x7C381010, 0x38383800),
    "6": int(0xFE103810, 0x38383800),
    "7": int(0xFE7C3810, 0x38383800),
    "8": int(0x38101010, 0x54547C00),
    "9": int(0x7C381010, 0x54547C00)
};