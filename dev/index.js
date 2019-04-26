/* JSLint edition 2019-01-31 */
/*jslint
    browser:true
*/
/*global
    Image, Math, bounding, build_bounding, build_image_region, build_region,
    click_in_box, document, draw_image, draw_image2, event_click, getPosition,
    get_box, get_click, load, main, make_handler, viewport
*/
/*property
    addEventListener, bounding_box, clientX, clientY, currentTarget, dimension,
    drawImage, getBoundingClientRect, getContext, getElementById, height, item,
    left, length, max, min, onload, path, position, push, ready, src, top,
    width, x, y
*/


//        {"path": "https://mdn.mozillademos.org/files/5397/rhino.jpg"},

var viewport = {};
var bounding = [];


function build_region(position, dimension) {
    "use strict";
    var region = {};
    region.position = {};
    region.position.x = position.x;
    region.position.y = position.y;
    region.dimension = {};
    region.dimension.x = dimension.x;
    region.dimension.y = dimension.y;
    region.bounding_box = {};
    region.bounding_box.x = {};
    region.bounding_box.x.min = position.x;
    region.bounding_box.x.max = position.x + dimension.x;
    region.bounding_box.y = {};
    region.bounding_box.y.min = position.y;
    region.bounding_box.y.max = position.y + dimension.y;
    return region;
}

function build_image_region(width, height) {
    "use strict";
    var position = {};
    position.x = 0;
    position.y = 0;
    var dimension = {};
    var max = Math.max(width, height);
    dimension.x = max;
    dimension.y = max;
    return build_region(position, dimension);
}

function build_bounding(count) {
    "use strict";
    var index_y;
    var index_x;
    var count_x = count;
    var count_y = count * 2;
    var object;
    var position = {};
    var dimension = {};
    index_y = count * 2;
    while (index_y > 0) {
        index_y -= 1;
        index_x = count;
        while (index_x > 0) {
            index_x -= 1;
            position.x = viewport.dimension.x + index_x * 1024 / count_x;
            position.y = index_y * 2048 / count_y;
            dimension.x = 1024 / count_x;
            dimension.y = 2048 / count_y;
            object = build_region(position, dimension);
            bounding.push(object);
        }
    }
}

var load = [
    {"ready": "false", "path": "null.jpg"},
    {"ready": "false", "path": "test.jpg"},
    {"ready": "false", "path": "test.jpg"},
    {"ready": "false", "path": "test1.jpg"},
    {"ready": "false", "path": "test2.jpg"},
    {"ready": "false", "path": "test3.png"},
    {"ready": "false", "path": "test4.gif"},
    {"ready": "false", "path": "test0.jpg"},
    {"ready": "false", "path": "demo.png"},
    {"ready": "false", "path": "skyrim.jpg"}
];

function draw_image2(context, image, source, destination) {
    "use strict";
    context.drawImage(
        image,
        source.position.x,
        source.position.y,
        source.dimension.x,
        source.dimension.y,
        destination.position.x,
        destination.position.y,
        destination.dimension.x,
        destination.dimension.y
    );
}


function draw_image(box, see) {
    "use strict";
    if (see === undefined) {
        see = load[0];
    }
    if (see.ready) {
        var canvas = document.getElementById("canvas");
        var context = canvas.getContext("2d");
        var image = see.item;
        var source = build_image_region(image.width, image.height);
        draw_image2(context, image, source, box);
    }
}


function click_in_box(mouse_click, image) {
    "use strict";
    var x = image.bounding_box.x;
    var y = image.bounding_box.y;
    var hit = mouse_click;
    return x.min <= hit.x && hit.x < x.max && y.min <= hit.y && hit.y < y.max;
}

function get_click(event) {
    "use strict";
    var canvas = event.currentTarget;
    var rect = canvas.getBoundingClientRect();
    var click = {};
    click.x = event.clientX - rect.left;
    click.y = event.clientY - rect.top;
    return click;
}

function get_box(event) {
    "use strict";
    var click = get_click(event);
    var item = 0;
    var index = bounding.length;
    while (index > 0) {
        index -= 1;
        if (click_in_box(click, bounding[index])) {
            item = index;
        }
    }
    return item;
}

event_click(false, false, "#load", function (ignore) {
    "use strict";
    var index = bounding.length;
    while (index > 0) {
        index -= 1;
        if (index < load.length) {
            draw_image(bounding[index], load[index]);
        }
    }
});

function make_handler(image, index) {
    "use strict";
    return function () {
        load[index].item = image;
        load[index].ready = true;
    };
}

function getPosition(event) {
    "use strict";
    var meme = get_box(event);
    draw_image(viewport, load[meme]);
}

function main() {
    "use strict";
    var canvas = document.getElementById("canvas");
    canvas.addEventListener("click", getPosition, false);
    //event_click_one_run("#canvas", getPosition);

    viewport = build_image_region(2048, 2048);
    build_bounding(3);

    var image;
    var index = load.length;
    while (index > 0) {
        index -= 1;
        image = new Image();
        image.src = load[index].path;
        image.onload = make_handler(image, index);
    }
}

main();
