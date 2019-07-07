import { EventType } from "./EventType";
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
        const selected = selectAll(selector);
        const type = "blur";
        const callback = eventTarget(method);
        const capture = bubblePhase();
        addEventListener(selected, type, callback, capture);
    }
    /*
    export function SelectAllEventTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = bubblePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectAllEventTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        addEventListener(selected);
    }
    export function SelectAllEventTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectAll(selector);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = capturePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const selected = selectFirst(selector);
        callback = currentTarget(method);
        capture = capturePhase();
        invokeNow(selected, method);
        addEventListener(selected);
    }
    */
}
