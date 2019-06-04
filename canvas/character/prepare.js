/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    character, character_code, character_name
*/
/*property
    code, name
*/
var character = {};
character.code = {};
character.name = {};
/**
 * @param {string} name
 */
function character_code(name) {
    var code = character.name[name];
    if (code === undefined) {
        /* assign default value */
        code = 0x0000;
    }
    return code;
}
/**
 * @param {number} code
 */
function character_name(code) {
    var name = character.code[code];
    if (name === undefined) {
        /* assign default value */
        name = "NULL";
    }
    return name;
}