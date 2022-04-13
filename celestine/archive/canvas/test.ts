import { character } from "./character/0000-007F";
import { EventListener } from "./event/EventListener";
import { EventType } from "./event/EventType";
import { font } from "./font/rune";
/* eslint-disable max-statements */
/* eslint-disable no-magic-numbers */
/* eslint-disable no-undef */
/* eslint-disable one-var */
/* eslint-disable prefer-const */
/* eslint-disable sort-vars */

const canvas = document.getElementsByTagName("canvas");
const log_font_x = 4;
const log_font_y = 4;
const log_glyph_x = 3;
const log_glyph_y = 3;
const log_page_x = 8;
const log_page_y = 8;
const log_pixel_x = 2;
const log_pixel_y = 0;


const size_font_x = 2 ** log_font_x;
const size_font_y = 2 ** log_font_y;
const size_glyph_x = 2 ** log_glyph_x;
const size_glyph_y = 2 ** log_glyph_y;
const size_page_x = 2 ** log_page_x;
const size_page_y = 2 ** log_page_y;
const size_pixel_x = 2 ** log_pixel_x;
const size_pixel_y = 2 ** log_pixel_y;

const unit_per_page_x = size_page_x * size_glyph_x * size_pixel_x;
const unit_per_page_y = size_page_y * size_glyph_y * size_pixel_y;
const unit_per_page = unit_per_page_x * unit_per_page_y;
const unit_per_glyph_x = size_glyph_x * size_pixel_x;
const unit_per_glyph_y = size_glyph_y * size_pixel_y;
const unit_per_glyph = unit_per_glyph_x * unit_per_glyph_y;

const unit_per_row = size_glyph_y * size_pixel_y * size_page_x * size_glyph_x * size_pixel_x;

const bitwise_extract_number_x = unit_per_glyph_x - 1;
const bitwise_extract_number_y = (unit_per_glyph_y - 1) << (log_glyph_x + log_pixel_x);


let data = null,
    indexX = 0,
    indexY = 0,
    off = 0,
    view = null;


/**
 * @param {HTMLCanvasElement} element
 */
const spat = function spat(element) {


    const context = element.getContext("2d"),
        { width } = element,
        { height } = element,
        imageData = context.createImageData(width, height);
    let yy = height;
    while (yy > 0) {

        yy -= 1;
        let xx = width;
        while (xx > 0) {

            xx -= 1;
            let index = imageData.width;
            index *= yy;
            index += xx;
            index *= 4;
            imageData.data[index + 0] = Math.random() * 256;
            imageData.data[index + 1] = Math.random() * 256;
            imageData.data[index + 2] = Math.random() * 256;
            imageData.data[index + 3] = 255;

        }

    }
    context.putImageData(imageData, 0, 0);
    return imageData;

    /*
     *Index_x = 25;
     *indexY = 25;
     *context.putImageData(imageData, 0, 0, indexX, indexY, 8, 8);
     */

};


/**
 * @param {HTMLCanvasElement} element
 */
const main = function main(element) {


    view = element.getContext("2d");
    data = view.createImageData(element.width, element.height);
    data = spat(element);
    view.putImageData(data, 0, 0);

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


function draw(art: Uint8Array) {
    const offset = unit_per_row * indexY;
    let index = unit_per_glyph;
    while (index > 0) {
        index -= 1;
        var font_x = size_font_x;
        while (font_x > 0) {
            font_x -= 1;
            var font_y = size_font_y;
            while (font_y > 0) {
                font_y -= 1;
                const extract_w = index & 0b00000011;
                const extract_x = index & 0b00011100;;
                const extract_y = index & 0b11100000;
                const scale_w = extract_w >>> 0x0;
                const scale_x = extract_x >>> 0x2;
                const scale_y = extract_y >>> 0x5;
                const position_w = scale_w;
                const position_x = size_pixel_x * (size_font_x * scale_x + font_x);
                const position_y = unit_per_page_x * (size_font_y * scale_y + font_y);
                const location = offset + position_x + position_y + position_w;
                data.data[location] = art[index];
            }
        }
    }
    view.putImageData(data, 0, 0);
}


/**
 * @param {number} input
 */
const paint64 = function paint64(input) {


    let glyph = input,
        index = 256;
    // eslint-disable-next-line no-undef
    const art = new Uint8Array(index);
    let bb = Math.random(),
        gg = Math.random(),
        rr = Math.random();
    bb *= 128;
    gg *= 128;
    rr *= 128;
    bb += 128;
    gg += 128;
    rr += 128;

    while (index >= 0) {

        index -= 4;
        // eslint-disable-next-line no-bitwise
        const bit = glyph & 1;
        art[index + 0] = rr * bit;
        art[index + 1] = gg * bit;
        art[index + 2] = bb * bit;
        art[index + 3] = 255;
        // eslint-disable-next-line no-bitwise
        glyph >>>= 1;

    }
    return art;

};


EventListener.SelectFirstEventTargetBubblePhaseInvokeLater("body", EventType.KeyboardEvent.keypress, (item) => {
    const key = item as KeyboardEvent;
    const char = key.keyCode;
    const code = character.range_0000_007F[char];
    const glyph = font.rune[code];
    if (typeof glyph !== "undefined") {
        draw(paint64(glyph));
    }
    indexX += 0;
    indexY += size_font_y;
});
/**
 * @param {number} glyph
 */
const out = function out(glyph) {


    draw(paint64(glyph));
    indexX += 1;
    off += 1;
    if (off % 8 === 0) {

        off = 0;
        indexX -= 8;
        indexY += 1;

    }
    if (indexY > 254) {

        indexY = 0;
        indexX += 9;

    }

};
out(0xFEA0BE80FE808000);
out(0xFE222E2A2A2A2A00);
out(0x0202FE02FA0AFE00);
out(0xA8A8A8A8E888FE00);
out(0xFE0AFA02FE020200);

