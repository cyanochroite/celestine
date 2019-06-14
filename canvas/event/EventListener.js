/* eslint-disable no-empty-function */
/* eslint-disable prefer-const */
/* eslint-disable sort-vars */
/* eslint-disable new-cap */
/* eslint-disable no-unused-expressions */
/* eslint-disable no-underscore-dangle */
/* eslint-disable max-params */
/* eslint-disable no-shadow */
/* eslint-disable func-style */
/* eslint-disable max-statements */
/* eslint-disable no-undef */
/* eslint-disable func-names */
/* eslint-disable max-len */

exports.__esModule = true;
const EventListener =

    /** @class */
    (function () {

        function EventListener () {
        }
        EventListener.addEventListener = function (selected, type, callback, capture) {

            selected.forEach((element) => {

                element.addEventListener(type, callback, capture);

            });

        };
        EventListener.EventTarget = function (method) {

            return function (event) {

                return method(event);

            };

        };
        EventListener.CurrentTarget = function (method) {

            return function (event) {

                return method(event.currentTarget);

            };

        };
        EventListener.InvokeLater = function (selected, method) {

            method;
            selected.forEach((element) => {

                element;

            });

        };
        EventListener.InvokeNow = function (selected, method) {

            selected.forEach((element) => {

                method(element);

            });

        };
        EventListener.BubblePhase = function () {

            return false;

        };
        EventListener.CapturePhase = function () {

            return true;

        };
        EventListener.SelectAll = function (selector) {

            const array = [];
            return array.slice.call(document.querySelectorAll(selector));

        };
        EventListener.SelectFirst = function (selector) {

            return [document.querySelector(selector)];

        };
        EventListener.prototype.SelectAllEventTargetBubblePhaseInvokeLater = function (selector, type, method) {

            const selected = EventListener.SelectAll(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectAllEventTargetBubblePhaseInvokeNow = function (selector, type, method) {

            const selected = EventListener.SelectAll(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectAllEventTargetCapturePhaseInvokeLater = function (selector, type, method) {

            const selected = EventListener.SelectAll(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectAllEventTargetCapturePhaseInvokeNow = function (selector, type, method) {

            const selected = EventListener.SelectAll(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectAllCurrentTargetBubblePhaseInvokeLater = function (selector, type, method) {

            const selected = EventListener.SelectAll(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectAllCurrentTargetBubblePhaseInvokeNow = function (selector, type, method) {

            const selected = EventListener.SelectAll(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectAllCurrentTargetCapturePhaseInvokeLater = function (selector, type, method) {

            const selected = EventListener.SelectAll(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectAllCurrentTargetCapturePhaseInvokeNow = function (selector, type, method) {

            let selected = EventListener.SelectAll(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstEventTargetBubblePhaseInvokeLater = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstEventTargetBubblePhaseInvokeNow = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstEventTargetCapturePhaseInvokeLater = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstEventTargetCapturePhaseInvokeNow = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.EventTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstCurrentTargetBubblePhaseInvokeLater = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstCurrentTargetBubblePhaseInvokeNow = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.BubblePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstCurrentTargetCapturePhaseInvokeLater = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeLater(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        EventListener.prototype.SelectFirstCurrentTargetCapturePhaseInvokeNow = function (selector, type, method) {

            let selected = EventListener.SelectFirst(selector),
                callback = EventListener.CurrentTarget(method),
                capture = EventListener.CapturePhase();
            EventListener.InvokeNow(selected, method);
            EventListener.addEventListener(selected, type, callback, capture);

        };
        return EventListener;

    }());
exports.EventListener = EventListener;
