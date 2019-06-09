/* eslint-disable one-var */
/* eslint-disable no-extra-parens */
/* eslint-disable no-param-reassign */
/* eslint-disable no-mixed-operators */
/* eslint-disable sort-vars */
/* eslint-disable no-undef */
/* eslint-disable prefer-const */
/* eslint-disable init-declarations */
/* eslint-disable id-length */
/* eslint-disable max-statements */
/* eslint-disable max-params */
/* eslint-disable no-magic-numbers */
/* eslint-disable no-bitwise */
/* eslint-disable no-implicit-globals */
/* eslint-disable camelcase */

let index_x = 0,
    index_y = 0,
    data,
    view,
    canvas = document.getElementsByTagName("canvas"),
    off = 0;


/**
 * @param {HTMLCanvasElement} element
 */
const spat = function spat (element) {

    "use strict";
    let context = element.getContext("2d"),
        {width} = element,
        {height} = element,
        image_data = context.createImageData(width, height),
        y = height,
        x,
        index;
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

    /*
     *Index_x = 25;
     *index_y = 25;
     *context.putImageData(imageData, 0, 0, index_x, index_y, 8, 8);
     */

};


/**
 * @param {HTMLCanvasElement} element
 */
const main = function main (element) {

    "use strict";
    view = element.getContext("2d");
    data = view.createImageData(element.width, element.height);
    data = spat(element);

};
spat(canvas[0]);
spat(canvas[1]);
spat(canvas[2]);
spat(canvas[3]);
spat(canvas[4]);
spat(canvas[5]);
spat(canvas[6]);
spat(canvas[7]);
main(canvas[3]);


/**
 * @param {any[] | Uint8Array} art
 */
const draw = function draw (art) {

    "use strict";
    let a = ((((((0x100 - index_y) << 0x3) - 0x1) << 0x8) + index_x) << 0x5),
        index = 256;
    while (index > 0) {

        index -= 1;
        data.data[a + (index & 31) - ((index >>> 5) << 13)] = art[index];

    }
    view.putImageData(data, 0, 0);

};

/**
 * @param {any[] | Uint8Array} art
 */
const buff = function buff (art) {

    "use strict";
    let a = ((((((0x100 - index_y) << 0x3) - 0x1) << 0x8) + index_x) << 0x5),
        index = 256;
    while (index > 0) {

        index -= 1;
        data.data[a + (index & 31) - ((index >>> 5) << 13)] = art[index];

    }

};


/**
 * @param {number} glyph
 */
const paint64 = function paint64 (glyph) {

    "use strict";
    let index = 256,
        art = new Uint8Array(index),
        r = Math.random() * 128 + 128,
        g = Math.random() * 128 + 128,
        b = Math.random() * 128 + 128,
        bit;
    while (index >= 0) {

        index -= 4;
        bit = glyph & 1;
        art[index + 0] = r * bit;
        art[index + 1] = g * bit;
        art[index + 2] = b * bit;
        art[index + 3] = 255;
        glyph >>>= 1;

    }
    return art;

};


document.addEventListener("keypress", (item) => {

    "use strict";
    let {key} = item,
        keycode = key.charCodeAt(0),
        name = character.code[keycode],
        glyph = font.rune[name];
    if (typeof glyph !== "undefined") {

        draw(paint64(glyph));

    }
    // Index_x += 0;
    index_y += 1;

});


/**
 * @param {number} glyph
 */
const out = function out (glyph) {

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

};
out(0xFEA0BE80FE808000);
out(0xFE222E2A2A2A2A00);
out(0x0202FE02FA0AFE00);
out(0xA8A8A8A8E888FE00);
out(0xFE0AFA02FE020200);

// View.putImageData(data, 0, 0);
