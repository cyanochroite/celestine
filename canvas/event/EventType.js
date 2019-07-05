import {EventListener} from "./EventListener";

class EventType {

    constructor () {

        this.AnimationEvent = {
            "animationcancel": "animationcancel",
            "animationend": "animationend",
            "animationiteration": "animationiteration",
            "animationstart": "animationstart"
        };

    }

}

new EventListener("blur").SelectFirstCurrentTargetBubblePhaseInvokeLater("#id", (element) => {

    // eslint-disable-next-line no-alert
    alert(element);

});
