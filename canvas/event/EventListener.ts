export class EventListener {
    private static EventTarget(method: (argument: Event) => void) {
        return (event: Event) => method(event);
    }
    private static CurrentTarget(method: (argument: EventTarget) => void) {
        return (event: Event) => method(event.currentTarget);
    }
    private static InvokeLater(selected, method) {
    }
    private static InvokeNow(selected, method) {
        selected.forEach((element) => {
            method(element);
        });
    }
    private static BubblePhase() {
        return false;
    }
    private static CapturePhase() {
        return true;
    }
    private static SelectAll(selector) {
        let array = [];
        return array.slice.call(document.querySelectorAll(selector));
    }
    private static SelectFirst(selector) {
        return [document.querySelector(selector)];
    }
    public SelectAllEventTargetBubblePhaseInvokeLater(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectAllEventTargetBubblePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(null, method);
    }
    public SelectAllEventTargetCapturePhaseInvokeLater(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectAllEventTargetCapturePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(null, method);
    }
    public SelectAllCurrentTargetBubblePhaseInvokeLater(type: any, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectAllCurrentTargetBubblePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(null, method);
    }
    public SelectAllCurrentTargetCapturePhaseInvokeLater(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectAllCurrentTargetCapturePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(null, method);
    }
    public SelectFirstEventTargetBubblePhaseInvokeLater(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectFirstEventTargetBubblePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(null, method);
    }
    public SelectFirstEventTargetCapturePhaseInvokeLater(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectFirstEventTargetCapturePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(null, method);
    }
    public SelectFirstCurrentTargetBubblePhaseInvokeLater(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectFirstCurrentTargetBubblePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(null, method);
    }
    public SelectFirstCurrentTargetCapturePhaseInvokeLater(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(null, method);
    }
    public SelectFirstCurrentTargetCapturePhaseInvokeNow(type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(method);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(null, method);
    }
}
