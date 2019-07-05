/* eslint-disable max-lines */
/* eslint-disable complexity */
/* eslint-disable func-names */
/* eslint-disable init-declarations */
/* eslint-disable max-len */
/* eslint-disable max-statements */
/* eslint-disable no-shadow */
/* eslint-disable no-undef */
/* eslint-disable no-unused-vars */
/* eslint-disable one-var */
// eslint-disable-next-line no-underscore-dangle
exports.__esModule = true;
let font;
(function (font) {

    let rune;
    (function (rune) {

        rune[rune.NULL = 0] = "NULL";
        rune[rune["START OF HEADING"] = 0] = "START OF HEADING";
        rune[rune["START OF TEXT"] = 0] = "START OF TEXT";
        rune[rune["END OF TEXT"] = 0] = "END OF TEXT";
        rune[rune["END OF TRANSMISSION"] = 0] = "END OF TRANSMISSION";
        rune[rune.ENQUIRY = 0] = "ENQUIRY";
        rune[rune.ACKNOWLEDGE = 0] = "ACKNOWLEDGE";
        rune[rune.BELL = 0] = "BELL";
        rune[rune.BACKSPACE = 0] = "BACKSPACE";
        rune[rune["CHARACTER TABULATION"] = 0] = "CHARACTER TABULATION";
        rune[rune["LINE FEED (LF)"] = 0] = "LINE FEED (LF)";
        rune[rune["LINE TABULATION"] = 0] = "LINE TABULATION";
        rune[rune["FORM FEED (FF)"] = 0] = "FORM FEED (FF)";
        rune[rune["CARRIAGE RETURN (CR)"] = 0] = "CARRIAGE RETURN (CR)";
        rune[rune["SHIFT OUT"] = 0] = "SHIFT OUT";
        rune[rune["SHIFT IN"] = 0] = "SHIFT IN";
        rune[rune["DATA LINK ESCAPE"] = 0] = "DATA LINK ESCAPE";
        rune[rune["DEVICE CONTROL ONE"] = 0] = "DEVICE CONTROL ONE";
        rune[rune["DEVICE CONTROL TWO"] = 0] = "DEVICE CONTROL TWO";
        rune[rune["DEVICE CONTROL THREE"] = 0] = "DEVICE CONTROL THREE";
        rune[rune["DEVICE CONTROL FOUR"] = 0] = "DEVICE CONTROL FOUR";
        rune[rune["NEGATIVE ACKNOWLEDGE"] = 0] = "NEGATIVE ACKNOWLEDGE";
        rune[rune["SYNCHRONOUS IDLE"] = 0] = "SYNCHRONOUS IDLE";
        rune[rune["END OF TRANSMISSION BLOCK"] = 0] = "END OF TRANSMISSION BLOCK";
        rune[rune.CANCEL = 0] = "CANCEL";
        rune[rune["END OF MEDIUM"] = 0] = "END OF MEDIUM";
        rune[rune.SUBSTITUTE = 0] = "SUBSTITUTE";
        rune[rune.ESCAPE = 0] = "ESCAPE";
        rune[rune["INFORMATION SEPARATOR FOUR (FS)"] = 0] = "INFORMATION SEPARATOR FOUR (FS)";
        rune[rune["INFORMATION SEPARATOR THREE (GS)"] = 0] = "INFORMATION SEPARATOR THREE (GS)";
        rune[rune["INFORMATION SEPARATOR TWO (RS)"] = 0] = "INFORMATION SEPARATOR TWO (RS)";
        rune[rune["INFORMATION SEPARATOR ONE (US)"] = 0] = "INFORMATION SEPARATOR ONE (US)";
        rune[rune.SPACE = 0] = "SPACE";
        rune[rune["EXCLAMATION MARK"] = 0] = "EXCLAMATION MARK";
        rune[rune["QUOTATION MARK"] = 0] = "QUOTATION MARK";
        rune[rune["NUMBER SIGN"] = 0] = "NUMBER SIGN";
        rune[rune["DOLLAR SIGN"] = 18314730673227235000] = "DOLLAR SIGN";
        rune[rune["PERCENT SIGN"] = 0] = "PERCENT SIGN";
        rune[rune.AMPERSAND = 0] = "AMPERSAND";
        rune[rune.APOSTROPHE = 0] = "APOSTROPHE";
        rune[rune["LEFT PARENTHESIS"] = 0] = "LEFT PARENTHESIS";
        rune[rune["RIGHT PARENTHESIS"] = 0] = "RIGHT PARENTHESIS";
        rune[rune.ASTERISK = 0] = "ASTERISK";
        rune[rune["PLUS SIGN"] = 0] = "PLUS SIGN";
        rune[rune.COMMA = 34995790082211840] = "COMMA";
        rune[rune["HYPHEN MINUS"] = 0] = "HYPHEN MINUS";
        rune[rune["FULL STOP"] = 18350759642045022000] = "FULL STOP";
        rune[rune.SOLIDUS = 18341066175265421000] = "SOLIDUS";
        rune[rune["DIGIT ZERO"] = 15780259870806032] = "DIGIT ZERO";
        rune[rune["DIGIT ONE"] = 8950921920573870000] = "DIGIT ONE";
        rune[rune["DIGIT TWO"] = 18307194126901187000] = "DIGIT TWO";
        rune[rune["DIGIT THREE"] = 18337593424385937000] = "DIGIT THREE";
        rune[rune["DIGIT FOUR"] = 4039746527600064500] = "DIGIT FOUR";
        rune[rune["DIGIT FIVE"] = 8950921921247590000] = "DIGIT FIVE";
        rune[rune["DIGIT SIX"] = 18307194127574907000] = "DIGIT SIX";
        rune[rune["DIGIT SEVEN"] = 18337593425059658000] = "DIGIT SEVEN";
        rune[rune["DIGIT EIGHT"] = 4039746528071679000] = "DIGIT EIGHT";
        rune[rune["DIGIT NINE"] = 8950921921719205000] = "DIGIT NINE";
        rune[rune.COLON = 0] = "COLON";
        rune[rune.SEMICOLON = 0] = "SEMICOLON";
        rune[rune["LESS THAN SIGN"] = 0] = "LESS THAN SIGN";
        rune[rune["EQUALS SIGN"] = 0] = "EQUALS SIGN";
        rune[rune["GREATER THAN SIGN"] = 0] = "GREATER THAN SIGN";
        rune[rune["QUESTION MARK"] = 18341059603084755000] = "QUESTION MARK";
        rune[rune["COMMERCIA AT"] = 0] = "COMMERCIA AT";
        rune[rune["LATIN CAPITAL LETTER A"] = 0] = "LATIN CAPITAL LETTER A";
        rune[rune["LATIN CAPITAL LETTER B"] = 0] = "LATIN CAPITAL LETTER B";
        rune[rune["LATIN CAPITAL LETTER C"] = 0] = "LATIN CAPITAL LETTER C";
        rune[rune["LATIN CAPITAL LETTER D"] = 0] = "LATIN CAPITAL LETTER D";
        rune[rune["LATIN CAPITAL LETTER E"] = 0] = "LATIN CAPITAL LETTER E";
        rune[rune["LATIN CAPITAL LETTER F"] = 0] = "LATIN CAPITAL LETTER F";
        rune[rune["LATIN CAPITAL LETTER G"] = 18338930948747360000] = "LATIN CAPITAL LETTER G";
        rune[rune["LATIN CAPITAL LETTER H"] = 0] = "LATIN CAPITAL LETTER H";
        rune[rune["LATIN CAPITAL LETTER I"] = 0] = "LATIN CAPITAL LETTER I";
        rune[rune["LATIN CAPITAL LETTER J"] = 0] = "LATIN CAPITAL LETTER J";
        rune[rune["LATIN CAPITAL LETTER K"] = 0] = "LATIN CAPITAL LETTER K";
        rune[rune["LATIN CAPITAL LETTER L"] = 0] = "LATIN CAPITAL LETTER L";
        rune[rune["LATIN CAPITAL LETTER M"] = 0] = "LATIN CAPITAL LETTER M";
        rune[rune["LATIN CAPITAL LETTER N"] = 0] = "LATIN CAPITAL LETTER N";
        rune[rune["LATIN CAPITAL LETTER O"] = 0] = "LATIN CAPITAL LETTER O";
        rune[rune["LATIN CAPITAL LETTER P"] = 0] = "LATIN CAPITAL LETTER P";
        rune[rune["LATIN CAPITAL LETTER Q"] = 0] = "LATIN CAPITAL LETTER Q";
        rune[rune["LATIN CAPITAL LETTER R"] = 18347867744898710000] = "LATIN CAPITAL LETTER R";
        rune[rune["LATIN CAPITAL LETTER S"] = 0] = "LATIN CAPITAL LETTER S";
        rune[rune["LATIN CAPITAL LETTER T"] = 0] = "LATIN CAPITAL LETTER T";
        rune[rune["LATIN CAPITAL LETTER U"] = 0] = "LATIN CAPITAL LETTER U";
        rune[rune["LATIN CAPITAL LETTER V"] = 0] = "LATIN CAPITAL LETTER V";
        rune[rune["LATIN CAPITAL LETTER W"] = 0] = "LATIN CAPITAL LETTER W";
        rune[rune["LATIN CAPITAL LETTER X"] = 0] = "LATIN CAPITAL LETTER X";
        rune[rune["LATIN CAPITAL LETTER Y"] = 0] = "LATIN CAPITAL LETTER Y";
        rune[rune["LATIN CAPITAL LETTER Z"] = 0] = "LATIN CAPITAL LETTER Z";
        rune[rune["LEFT SQUARE BRACKET"] = 0] = "LEFT SQUARE BRACKET";
        rune[rune["REVERSE SOLIDUS"] = 0] = "REVERSE SOLIDUS";
        rune[rune["RIGHT SQUARE BRACKET"] = 0] = "RIGHT SQUARE BRACKET";
        rune[rune["CIRCUMFLEX ACCENT"] = 0] = "CIRCUMFLEX ACCENT";
        rune[rune["LOW LINE"] = 0] = "LOW LINE";
        rune[rune["GRAVE ACCENT"] = 0] = "GRAVE ACCENT";
        rune[rune["LATIN SMALL LETTER A"] = 0] = "LATIN SMALL LETTER A";
        rune[rune["LATIN SMALL LETTER B"] = 18339482904389804000] = "LATIN SMALL LETTER B";
        rune[rune["LATIN SMALL LETTER C"] = 0] = "LATIN SMALL LETTER C";
        rune[rune["LATIN SMALL LETTER D"] = 18341171728379600000] = "LATIN SMALL LETTER D";
        rune[rune["LATIN SMALL LETTER E"] = 18347874479507538000] = "LATIN SMALL LETTER E";
        rune[rune["LATIN SMALL LETTER F"] = 18341059603359896000] = "LATIN SMALL LETTER F";
        rune[rune["LATIN SMALL LETTER G"] = 0] = "LATIN SMALL LETTER G";
        rune[rune["LATIN SMALL LETTER H"] = 0] = "LATIN SMALL LETTER H";
        rune[rune["LATIN SMALL LETTER I"] = 0] = "LATIN SMALL LETTER I";
        rune[rune["LATIN SMALL LETTER J"] = 0] = "LATIN SMALL LETTER J";
        rune[rune["LATIN SMALL LETTER K"] = 0] = "LATIN SMALL LETTER K";
        rune[rune["LATIN SMALL LETTER L"] = 0] = "LATIN SMALL LETTER L";
        rune[rune["LATIN SMALL LETTER M"] = 0] = "LATIN SMALL LETTER M";
        rune[rune["LATIN SMALL LETTER N"] = 0] = "LATIN SMALL LETTER N";
        rune[rune["LATIN SMALL LETTER O"] = 0] = "LATIN SMALL LETTER O";
        rune[rune["LATIN SMALL LETTER P"] = 0] = "LATIN SMALL LETTER P";
        rune[rune["LATIN SMALL LETTER Q"] = 18348419837274915000] = "LATIN SMALL LETTER Q";
        rune[rune["LATIN SMALL LETTER R"] = 18347841494058074000] = "LATIN SMALL LETTER R";
        rune[rune["LATIN SMALL LETTER S"] = 0] = "LATIN SMALL LETTER S";
        rune[rune["LATIN SMALL LETTER T"] = 18341097132783600000] = "LATIN SMALL LETTER T";
        rune[rune["LATIN SMALL LETTER U"] = 0] = "LATIN SMALL LETTER U";
        rune[rune["LATIN SMALL LETTER V"] = 0] = "LATIN SMALL LETTER V";
        rune[rune["LATIN SMALL LETTER W"] = 0] = "LATIN SMALL LETTER W";
        rune[rune["LATIN SMALL LETTER X"] = 0] = "LATIN SMALL LETTER X";
        rune[rune["LATIN SMALL LETTER Y"] = 18341059603361604000] = "LATIN SMALL LETTER Y";
        rune[rune["LATIN SMALL LETTER Z"] = 0] = "LATIN SMALL LETTER Z";
        rune[rune["LEFT CURLY BRACKET"] = 0] = "LEFT CURLY BRACKET";
        rune[rune["VERTICAL LINE"] = 0] = "VERTICAL LINE";
        rune[rune["RIGHT CURLY BRACKET"] = 0] = "RIGHT CURLY BRACKET";
        rune[rune.TILDE = 0] = "TILDE";
        rune[rune.DELETE = 0] = "DELETE";

    }(rune = font.rune || (font.rune = {})));

}(font = exports.font || (exports.font = {})));
