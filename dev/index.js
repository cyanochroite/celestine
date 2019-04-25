/* JSLint edition 2019-01-31 */
/*jslint
    browser:true
*/
/*global
    Image, Math, bounding, build_bounding, document, draw_image, event_click,
    getPosition, get_box, load, main, make_handler, viewport
*/
/*property
    addEventListener, clientX, clientY, drawImage, getBoundingClientRect,
    getContext, getElementById, height, item, left, length, max, onload, path,
    push, ready, size_x, size_y, src, top, width, x, y
*/



//        {"path": "https://mdn.mozillademos.org/files/5397/rhino.jpg"},

var viewport = {};
viewport.x = 0;
viewport.y = 0;
viewport.size_x = 2048;
viewport.size_y = 2048;
var bounding = [];



function build_bounding(count) {
    "use strict";
    var index_y;
    var index_x;
    var count_x = count;
    var count_y = count * 2;
    var object;
    index_y = count * 2;
    while (index_y > 0) {
        index_y -= 1;
        index_x = count;
        while (index_x > 0) {
            index_x -= 1;
            object = {};
            object.x = viewport.size_x + index_x * 1024 / count_x;
            object.y = index_y * 2048 / count_y;
            object.size_x = 1024 / count_x;
            object.size_y = 2048 / count_y;	
//            object.x_max = object.x_min + object.size_x;
//            object.y_max = index_y * 2048 / count_y;
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
    {"ready": "false", "path": "demo.png"}
];

function draw_image(box, see) {
    "use strict";
    if (see === undefined) {
        see = load[0];
    }
    if (see.ready) {
        var canvas = document.getElementById("canvas");
        var context = canvas.getContext("2d");
        var image = see.item;
        context.drawImage(
            image,
            0,
            0,
            image.width * Math.max(image.height / image.width, 1),
            image.height * Math.max(image.width / image.height, 1),
            box.x,
            box.y,
            box.size_x,
            box.size_y
        );
    }
}


function get_box2(click, box) {
    "use strict";
    if (
        click.x >= box.x
        && click.y >= box.y
        && click.x <= box.x + box.size_x
        && click.y <= box.y + box.size_y
    ) {
        return true;
    }
    return false;
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
        if (get_box2(click, bounding[index])) {
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
