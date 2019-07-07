
exports.__esModule = true;
/* eslint-disable func-names */
/* eslint-disable func-style */
/* eslint-disable init-declarations */
/* eslint-disable max-len */
/* eslint-disable max-params */
/* eslint-disable max-statements */
/* eslint-disable no-shadow */
/* eslint-disable no-unused-vars */
let EventListener;
(function (EventListener) {

    function eventTarget (method) {

        return function (event) {

            return method(event);

        };

    }
    function currentTarget (method) {

        return function (event) {

            return method(event.currentTarget);

        };

    }
    function invokeNow (selected, method) {

        selected.forEach((element) => {

            method(element);

        });

    }
    function bubblePhase () {

        return false;

    }
    function capturePhase () {

        return true;

    }
    function selectAll (selector) {

        return [].slice.call(document.querySelectorAll(selector));

    }
    function selectFirst (selector) {

        return [document.querySelector(selector)];

    }
    function addEventListener (selected, type, callback, capture) {

        selected.forEach((element) => {

            element.addEventListener(type, callback, capture);

        });

    }
    function SelectAllEventTargetBubblePhaseInvokeLater (selector, method) {

        const callback = eventTarget(method),
            capture = bubblePhase(),
            selected = selectAll(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllEventTargetBubblePhaseInvokeLater = SelectAllEventTargetBubblePhaseInvokeLater;
    function SelectAllEventTargetBubblePhaseInvokeNow (selector, method) {

        const callback = eventTarget(method),
            capture = bubblePhase(),
            selected = selectAll(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllEventTargetBubblePhaseInvokeNow = SelectAllEventTargetBubblePhaseInvokeNow;
    function SelectAllEventTargetCapturePhaseInvokeLater (selector, method) {

        const callback = eventTarget(method),
            capture = capturePhase(),
            selected = selectAll(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllEventTargetCapturePhaseInvokeLater = SelectAllEventTargetCapturePhaseInvokeLater;
    function SelectAllEventTargetCapturePhaseInvokeNow (selector, method) {

        const callback = eventTarget(method),
            capture = capturePhase(),
            selected = selectAll(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllEventTargetCapturePhaseInvokeNow = SelectAllEventTargetCapturePhaseInvokeNow;
    function SelectAllCurrentTargetBubblePhaseInvokeLater (selector, method) {

        const callback = currentTarget(method),
            capture = bubblePhase(),
            selected = selectAll(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllCurrentTargetBubblePhaseInvokeLater = SelectAllCurrentTargetBubblePhaseInvokeLater;
    function SelectAllCurrentTargetBubblePhaseInvokeNow (selector, method) {

        const callback = currentTarget(method),
            capture = bubblePhase(),
            selected = selectAll(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllCurrentTargetBubblePhaseInvokeNow = SelectAllCurrentTargetBubblePhaseInvokeNow;
    function SelectAllCurrentTargetCapturePhaseInvokeLater (selector, method) {

        const callback = currentTarget(method),
            capture = capturePhase(),
            selected = selectAll(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllCurrentTargetCapturePhaseInvokeLater = SelectAllCurrentTargetCapturePhaseInvokeLater;
    function SelectAllCurrentTargetCapturePhaseInvokeNow (selector, method) {

        const callback = currentTarget(method),
            capture = capturePhase(),
            selected = selectAll(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectAllCurrentTargetCapturePhaseInvokeNow = SelectAllCurrentTargetCapturePhaseInvokeNow;
    function SelectFirstEventTargetBubblePhaseInvokeLater (selector, method) {

        const callback = eventTarget(method),
            capture = bubblePhase(),
            selected = selectFirst(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstEventTargetBubblePhaseInvokeLater = SelectFirstEventTargetBubblePhaseInvokeLater;
    function SelectFirstEventTargetBubblePhaseInvokeNow (selector, method) {

        const callback = eventTarget(method),
            capture = bubblePhase(),
            selected = selectFirst(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstEventTargetBubblePhaseInvokeNow = SelectFirstEventTargetBubblePhaseInvokeNow;
    function SelectFirstEventTargetCapturePhaseInvokeLater (selector, method) {

        const callback = eventTarget(method),
            capture = capturePhase(),
            selected = selectFirst(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstEventTargetCapturePhaseInvokeLater = SelectFirstEventTargetCapturePhaseInvokeLater;
    function SelectFirstEventTargetCapturePhaseInvokeNow (selector, method) {

        const callback = eventTarget(method),
            capture = capturePhase(),
            selected = selectFirst(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstEventTargetCapturePhaseInvokeNow = SelectFirstEventTargetCapturePhaseInvokeNow;
    function SelectFirstCurrentTargetBubblePhaseInvokeLater (selector, method) {

        const callback = currentTarget(method),
            capture = bubblePhase(),
            selected = selectFirst(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstCurrentTargetBubblePhaseInvokeLater = SelectFirstCurrentTargetBubblePhaseInvokeLater;
    function SelectFirstCurrentTargetBubblePhaseInvokeNow (selector, method) {

        const callback = currentTarget(method),
            capture = bubblePhase(),
            selected = selectFirst(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstCurrentTargetBubblePhaseInvokeNow = SelectFirstCurrentTargetBubblePhaseInvokeNow;
    function SelectFirstCurrentTargetCapturePhaseInvokeLater (selector, method) {

        const callback = currentTarget(method),
            capture = capturePhase(),
            selected = selectFirst(selector),
            type = "blur";
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstCurrentTargetCapturePhaseInvokeLater = SelectFirstCurrentTargetCapturePhaseInvokeLater;
    function SelectFirstCurrentTargetCapturePhaseInvokeNow (selector, method) {

        const callback = currentTarget(method),
            capture = capturePhase(),
            selected = selectFirst(selector),
            type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);

    }
    EventListener.SelectFirstCurrentTargetCapturePhaseInvokeNow = SelectFirstCurrentTargetCapturePhaseInvokeNow;

}(EventListener = exports.EventListener || (exports.EventListener = {})));
