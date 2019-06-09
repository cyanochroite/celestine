// eslint-disable-next-line prefer-const
let character = {};
character.code = {};
character.name = {};
// eslint-disable-next-line no-unused-vars
const characterCode =

    /**
     * @param {string} name
     */
    function characterCode (name) {

        "use strict";
        let code = character.name[name];
        if (typeof code === "undefined") {

            // eslint-disable-next-line no-magic-numbers
            code = 0x0000;

        }
        return code;

    },
    // eslint-disable-next-line no-unused-vars
    characterName =

        /**
         * @param {number} code
         */
        function characterName (code) {

            "use strict";
            let name = character.code[code];
            if (typeof name === "undefined") {

                name = "NULL";

            }
            return name;

        };
