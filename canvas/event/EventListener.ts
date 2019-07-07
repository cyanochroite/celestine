import { EventType } from "./EventType";
/* eslint-disable func-names */
/* eslint-disable func-style */
/* eslint-disable init-declarations */
/* eslint-disable max-len */
/* eslint-disable max-params */
/* eslint-disable max-statements */
/* eslint-disable no-shadow */
/* eslint-disable no-unused-vars */
export namespace EventListener {
    function eventTarget(method: (argument: Event) => void) {
        return (event: Event) => method(event);
    }
    function currentTarget(method: (argument: EventTarget) => void) {
        return (event: Event) => method(event.currentTarget);
    }
    function invokeNow(selected: Element[], method: (argument: Event | EventTarget) => void) {
        selected.forEach((element: Element) => {
            method(element);
        });
    }
    function bubblePhase() {
        return false;
    }
    function capturePhase() {
        return true;
    }
    function selectAll(selector: string) {
        return [].slice.call(document.querySelectorAll(selector));
    }
    function selectFirst(selector: string) {
        return [document.querySelector(selector)];
    }
    function addEventListener(selected: Element[], type: string, callback: (event: Event) => void, capture: boolean) {
        selected.forEach((element: Element) => {
            element.addEventListener(type, callback, capture);
        });
    }
    export function SelectAllEventTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = bubblePhase();
        const selected = selectAll(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectAllEventTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = bubblePhase();
        const selected = selectAll(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    export function SelectAllEventTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = capturePhase();
        const selected = selectAll(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectAllEventTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = capturePhase();
        const selected = selectAll(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    export function SelectAllCurrentTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = bubblePhase();
        const selected = selectAll(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectAllCurrentTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = bubblePhase();
        const selected = selectAll(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    export function SelectAllCurrentTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = capturePhase();
        const selected = selectAll(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectAllCurrentTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = capturePhase();
        const selected = selectAll(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstEventTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = bubblePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstEventTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = bubblePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstEventTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = capturePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstEventTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = eventTarget(method);
        const capture = capturePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstCurrentTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = bubblePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstCurrentTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = bubblePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstCurrentTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = capturePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        addEventListener(selected, type, callback, capture);
    }
    export function SelectFirstCurrentTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const callback = currentTarget(method);
        const capture = capturePhase();
        const selected = selectFirst(selector);
        const type = "blur";
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
}
