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

/**
 * @param {(arg0: string) => void} callback
 */

var element = document.getElementsByTagName("canvas");
spat(element[0]);
spat(element[1]);
spat(element[2]);
spat(element[3]);
spat(element[4]);
spat(element[5]);
spat(element[6]);
spat(element[7]);
main(element[3]);


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

/**
 * @param {HTMLCanvasElement} element
 */
function spat(element) {
    "use strict";
    var context = element.getContext("2d");
    var width = element.width;
    var height = element.height;
    var image_data = context.createImageData(width, height);
    var y = height;
    var x;
    var index;
    while (y > 0) {
        y -= 1;
        x = width;
        while (x > 0) {
            x -= 1;
            index = (x + y * image_data.width) * 4;
            image_data.data[index + 0] = Math.random() * 256;
            image_data.data[index + 1] = Math.random() * 256;
            image_data.data[index + 2] = Math.random() * 256;
            image_data.data[index + 3] = 255;
        }
    }
    context.putImageData(image_data, 0, 0);
    return image_data;
    //index_x = 25;
    //index_y = 25;
    //context.putImageData(imageData, 0, 0, index_x, index_y, 8, 8);
}


/**
 * @param {any[] | Uint8Array} art
 */
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
/**
 * @param {any[] | Uint8Array} art
 */
function buff(art) {
    "use strict";
    var a = ((((((0x100 - index_y) << 0x3) - 0x1) << 0x8) + index_x) << 0x5);
    var index = 256;
    while (index > 0) {
        index -= 1;
        data.data[a + (index & 31) - ((index >>> 5) << 13)] = art[index];
    }
}


/**
 * @param {HTMLCanvasElement} element
 */
function main(element) {
    "use strict";
    view = element.getContext("2d");
    data = view.createImageData(element.width, element.height);
    data = spat(element);
}

/**
 * @param {{ hi: any; lo: any; }} number
 */
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

/**
 * @param {number} glyph
 */
function paint64(glyph) {
    "use strict";
    var index = 256;
    var art = new Uint8Array(index);
    var r = Math.random() * 128 + 128;
    var g = Math.random() * 128 + 128;
    var b = Math.random() * 128 + 128;
    var bit;
    while (index >= 0) {
        index -= 4;
        bit = glyph & 1;
        art[index + 0] = r * bit;
        art[index + 1] = g * bit;
        art[index + 2] = b * bit;
        art[index + 3] = 255;
        glyph = glyph >>> 1;
    }
    return art;
}



document.addEventListener("keypress", function (item) {
    "use strict";
    var key = item.key;
    var keycode = key.charCodeAt(0);
    var hex = keycode.toString(16);
    var value = "0x00" + hex;
    var name = CHARACTER_NAME[value];
    var stuff = FONT[name];
    var glyph = parseInt(stuff, 16);
    if (glyph !== undefined) {
        draw(paint64(glyph));
    }
    //index_x += 0;
    index_y += 1;
});

var off = 0;

/**
 * @param {number} glyph
 */
function out(glyph) {
    "use strict";
    buff(paint64(glyph));
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
out(0xFEA0BE80FE808000);
out(0xFE222E2A2A2A2A00);
out(0x0202FE02FA0AFE00);
out(0xA8A8A8A8E888FE00);
out(0xFE0AFA02FE020200);

//view.putImageData(data, 0, 0);

