/* JSLint edition 2019-01-31 */
/*jslint
    bitwise:true, browser:true
*/
/*global
    Image, Math, Uint8Array, buff, data, document, draw, element, index_x,
    index_y, int, load, main, off, out, paint, spat, type, view
*/
/*property
    addEventListener, createImageData, data, drawImage, getContext,
    getElementsByTagName, height, hi, key, lo, max, onload, putImageData,
    random, src, width
*/

var index_x = 0;
var index_y = 0;
var data;
var view;

function int(hi, lo) {
    "use strict";
    var out = {};
    out.hi = hi;
    out.lo = lo;
    return out;
}

function load(element, path) {
    "use strict";
    var img = new Image();
    var width = element.width;
    var height = element.height;
    img.src = path;
    var ctx = element.getContext("2d");
    img.onload = function () {
        var x = 0;
        var y = height - img.height;
        x += Math.max(0, width - img.width) / 2;
        y -= Math.max(0, height - img.height) / 2;
        ctx.drawImage(img, x, y);
    };
}

function spat(element) {
    "use strict";
    var context = element.getContext("2d");
    var width = element.width;
    var height = element.height;
    var imageData = context.createImageData(width, height);
    var y = height;
    var x;
    var index;
    while (y > 0) {
        y -= 1;
        x = width;
        while (x > 0) {
            x -= 1;
            index = (x + y * imageData.width) * 4;
            imageData.data[index + 0] = Math.random() * 256;
            imageData.data[index + 1] = Math.random() * 256;
            imageData.data[index + 2] = Math.random() * 256;
            imageData.data[index + 3] = 255;
        }
    }
    context.putImageData(imageData, 0, 0);
    return imageData;
    //index_x = 25;
    //index_y = 25;
    //context.putImageData(imageData, 0, 0, index_x, index_y, 8, 8);
}


function draw(art) {
    "use strict";
    var a = ((((((0x100 - index_y) << 0x3) - 0x1) << 0x8) + index_x) << 0x5);
    var index = 256;
    while (index > 0) {
        index -= 1;
        data.data[a + (index & 31) - ((index >>> 5) << 13)] = art[index];
    }
    view.putImageData(data, 0, 0);
}
function buff(art) {
    "use strict";
    var a = ((((((0x100 - index_y) << 0x3) - 0x1) << 0x8) + index_x) << 0x5);
    var index = 256;
    while (index > 0) {
        index -= 1;
        data.data[a + (index & 31) - ((index >>> 5) << 13)] = art[index];
    }
}

var element = document.getElementsByTagName("canvas");
spat(element[0], 100);
spat(element[1], 10000);
spat(element[2], 10000);
spat(element[3], 10000);

spat(element[4], 100);
spat(element[5], 10000);
spat(element[6], 10000);
spat(element[7], 100000);

function main(element) {
    "use strict";
    view = element.getContext("2d");
    data = view.createImageData(element.width, element.height);
    data = spat(element);
}

main(element[3]);

function type(key) {
    "use strict";
    var out = {};
    out.hi = 0x00000000;
    out.lo = 0x00000000;
    switch (key) {
        case ",":
            return int(0x007C547C, 0x547C0000);
        case ".":
            return int(0xFEAAFEAA, 0xFEAAFE00);
        case "$":
            return int(0xFE2AFE82, 0xFEA8FE00);

        case "?":
            //return int(0xFE888888, 0x8E82BE00);
            return int(0xFE888888, 0xAE223E00);
        case "/":
            return int(0xFE888E82, 0xE2A0B800);


        case "a":
            return int(0x00000000, 0x00000000);
        case "b":
            return int(0xFE82EE88, 0xE880E000);
        case "c":
            return int(0x00000000, 0x00000000);
        case "d":
            return int(0xFE88EE82, 0xE280E000);
        case "e":
            return int(0xFEA0BEA0, 0xBE808000);
        case "f":
            return int(0xFE888888, 0xBE888E00);
        case "g":
            return int(0xFEA2AEA0, 0xBE808000);
        case "h":
            return int(0x00000000, 0x00000000);
        case "i":
            return int(0x00000000, 0x00000000);
        case "j":
            return int(0x00000000, 0x00000000);
        case "k":
            return int(0x00000000, 0x00000000);
        case "l":
            return int(0x00000000, 0x00000000);
        case "m":
            return int(0x00000000, 0x00000000);
        case "n":
            return int(0x00000000, 0x00000000);
        case "o":
            return int(0x00000000, 0x00000000);
        case "p":
            return int(0x00000000, 0x00000000);
        case "q":
            return int(0x00000000, 0x00000000);
        case "r":
            return int(0xFEA0A0A0, 0xB880FE00);
        case "s":
            return int(0x00000000, 0x00000000);
        case "t":
            return int(0xFE88AAAA, 0xBE808000);
        case "u":
            return int(0x00000000, 0x00000000);
        case "v":
            return int(0x00000000, 0x00000000);
        case "w":
            return int(0x00000000, 0x00000000);
        case "x":
            return int(0x00000000, 0x00000000);
        case "y":
            return int(0xFE888888, 0xBEA2A200);
        case "z":
            return int(0x00000000, 0x00000000);
        ////////
        case "A":
            return int(0x00000000, 0x00000000);
        case "B":
            return int(0x00000000, 0x00000000);
        case "C":
            return int(0x00000000, 0x00000000);
        case "D":
            return int(0x00000000, 0x00000000);
        case "E":
            return int(0x00000000, 0x00000000);
        case "F":
            return int(0xFEA0A0A0, 0xB8A0BE00);
        case "G":
            return int(0xFE80F888, 0xB880F800);
        case "H":
            return int(0x00000000, 0x00000000);
        case "I":
            return int(0x00000000, 0x00000000);
        case "J":
            return int(0x00000000, 0x00000000);
        case "K":
            return int(0x00000000, 0x00000000);
        case "L":
            return int(0x00000000, 0x00000000);
        case "M":
            return int(0x00000000, 0x00000000);
        case "N":
            return int(0x00000000, 0x00000000);
        case "O":
            return int(0x00000000, 0x00000000);
        case "P":
            return int(0x00000000, 0x00000000);
        case "Q":
            return int(0x00000000, 0x00000000);
        case "R":
            return int(0xFEA0B880, 0xB888F800);
        case "S":
            return int(0x00000000, 0x00000000);
        case "T":
            return int(0x00000000, 0x00000000);
        case "U":
            return int(0x00000000, 0x00000000);
        case "V":
            return int(0x00000000, 0x00000000);
        case "W":
            return int(0x00000000, 0x00000000);
        case "X":
            return int(0x00000000, 0x00000000);
        case "Y":
            return int(0x00000000, 0x00000000);
        case "Z":
            return int(0x00000000, 0x00000000);
        case "0":
            return int(0x38101010, 0x10101000);
        case "1":
            return int(0x7C381010, 0x10101000);
        case "2":
            return int(0xFE103810, 0x10101000);
        case "3":
            return int(0xFE7C3810, 0x10101000);
        case "4":
            return int(0x38101010, 0x38383800);
        case "5":
            return int(0x7C381010, 0x38383800);
        case "6":
            return int(0xFE103810, 0x38383800);
        case "7":
            return int(0xFE7C3810, 0x38383800);
        case "8":
            return int(0x38101010, 0x54547C00);
        case "9":
            return int(0x7C381010, 0x54547C00);
        case "End":
            return int(0xFE103810, 0x54547C00);
        case "ArrowDown":
            return int(0xFE7C3810, 0x54547C00);
        case "PageDown":
            return int(0x38101010, 0x9292FE00);
        case "ArrowLeft":
            return int(0x7C381010, 0x9292FE00);
        case "Clear":
            return int(0xFE103810, 0x9292FE00);
        case "ArrowRight":
            return int(0xFE7C3810, 0x54547C00);

    }
    return out;
}

function paint(number) {
    "use strict";
    var high = number.hi;
    var low = number.lo;
    //high = high & 0xAA00AA00;
    //low = low & 0xAA00AA00;
    //high = high & 0xFEAAFEAA;
    //low = low & 0xFEAAFE00;
    var index = 256;
    var art = new Uint8Array(index);
    var r = Math.random() * 128 + 128;
    var g = Math.random() * 128 + 128;
    var b = Math.random() * 128 + 128;
    var bit;
    while (index >= 128) {
        index -= 4;
        bit = low & 1;
        art[index + 0] = r * bit;
        art[index + 1] = g * bit;
        art[index + 2] = b * bit;
        art[index + 3] = 255;
        low = low >>> 1;
    }
    while (index >= 0) {
        bit = high & 1;
        art[index + 0] = r * bit;
        art[index + 1] = g * bit;
        art[index + 2] = b * bit;
        art[index + 3] = 255;
        high = high >>> 1;
        index -= 4;
    }
    return art;
}



document.addEventListener("keydown", function (item) {
    "use strict";
    draw(paint(type(item.key)));
    //index_x += 0;
    index_y += 1;
});

var off = 0;

function out(high, low) {
    "use strict";
    buff(paint(int(high, low)));
    index_x += 1;
    off += 1;
    if (off % 8 === 0) {
        off = 0;
        index_x -= 8;
        index_y += 1;
    }
    if (index_y > 254) {
        index_y = 0;
        index_x += 9;
    }
}
out(0xFEA0BE80, 0xFE808000);
out(0xFE222E2A, 0x2A2A2A00);
out(0x0202FE02, 0xFA0AFE00);
out(0xA8A8A8A8, 0xE888FE00);
out(0xFE0AFA02, 0xFE020200);

view.putImageData(data, 0, 0);