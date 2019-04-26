/* JSLint edition 2019-01-31 */
/*jslint
    browser:true
*/
/*global
    Image, Math, bounding, build_bounding, build_image, click_in_box, document,
    draw_image, draw_image2, event_click, getPosition, get_box, get_click, load,
    main, make_handler, viewport
*/
/*property
    addEventListener, bounding_box, box, clientX, clientY, currentTarget,
    dimension, drawImage, getBoundingClientRect, getContext, getElementById,
    height, item, left, length, max, min, onload, path, position, push, ready,
    size_x, size_y, src, top, width, x, y
*/



//        {"path": "https://mdn.mozillademos.org/files/5397/rhino.jpg"},

var viewport = {};
var bounding = [];


function build_image(position, dimension) {
    "use strict";
    var image = {};
    image.position = {};
    image.position.x = position.x;
    image.position.y = position.y;
    image.dimension = {};
    image.dimension.x = dimension.x;
    image.dimension.y = dimension.y;
    image.bounding_box = {};
    image.bounding_box.x = {};
    image.bounding_box.x.min = position.x;
    image.bounding_box.x.max = position.x + dimension.x;
    image.bounding_box.y = {};
    image.bounding_box.y.min = position.y;
    image.bounding_box.y.max = position.y + dimension.y;
    return image;
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
            object = build_image(position, dimension);
            bounding.push(object);
        }
    }
}

function build_viewport() {
    "use strict";
    var position = {};
    position.x = 0;
    position.y = 0;
    var dimension = {};
    dimension.x = 2048;
    dimension.y = 2048;
    viewport = build_image(position, dimension);
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
    {"ready": "false", "path": "demo.png"}
];

function draw_image2(context, image, source, destination) {
    "use strict";
    return context.drawImage(
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
        var position = {};
        position.x = 0;
        position.y = 0;
        var dimension = {};
        dimension.x = image.width * Math.max(image.height / image.width, 1);
        dimension.y = image.width * Math.max(image.height / image.width, 1);
        var source = build_image(position, dimension);
        draw_image2(context, image, source, box);
    }
}


function click_in_box(mouse_click, bounding_box) {
    "use strict";
    var min = bounding_box.box.min;
    var max = bounding_box.box.max;
    var hit = mouse_click;
    return min.x <= hit.x && hit.x < max.x && min.y <= hit.y && hit.y < max.y;
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

    build_viewport();
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
