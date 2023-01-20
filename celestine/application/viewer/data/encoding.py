"""Map character code points to an internal reprensentation."""
from celestine.unicode import NULL
from celestine.unicode import START_OF_HEADING
from celestine.unicode import START_OF_TEXT
from celestine.unicode import END_OF_TEXT
from celestine.unicode import END_OF_TRANSMISSION
from celestine.unicode import ENQUIRY
from celestine.unicode import ACKNOWLEDGE
from celestine.unicode import BELL
from celestine.unicode import BACKSPACE
from celestine.unicode import CHARACTER_TABULATION
from celestine.unicode import LINE_FEED
from celestine.unicode import LINE_TABULATION
from celestine.unicode import FORM_FEED
from celestine.unicode import CARRIAGE_RETURN
from celestine.unicode import SHIFT_OUT
from celestine.unicode import SHIFT_IN
from celestine.unicode import DATA_LINK_ESCAPE
from celestine.unicode import DEVICE_CONTROL_ONE
from celestine.unicode import DEVICE_CONTROL_TWO
from celestine.unicode import DEVICE_CONTROL_THREE
from celestine.unicode import DEVICE_CONTROL_FOUR
from celestine.unicode import NEGATIVE_ACKNOWLEDGE
from celestine.unicode import SYNCHRONOUS_IDLE
from celestine.unicode import END_OF_TRANSMISSION_BLOCK
from celestine.unicode import CANCEL
from celestine.unicode import END_OF_MEDIUM
from celestine.unicode import SUBSTITUTE
from celestine.unicode import ESCAPE
from celestine.unicode import INFORMATION_SEPARATOR_FOUR
from celestine.unicode import INFORMATION_SEPARATOR_THREE
from celestine.unicode import INFORMATION_SEPARATOR_TWO
from celestine.unicode import INFORMATION_SEPARATOR_ONE
from celestine.unicode import SPACE
from celestine.unicode import EXCLAMATION_MARK
from celestine.unicode import QUOTATION_MARK
from celestine.unicode import NUMBER_SIGN
from celestine.unicode import DOLLAR_SIGN
from celestine.unicode import PERCENT_SIGN
from celestine.unicode import AMPERSAND
from celestine.unicode import APOSTROPHE
from celestine.unicode import LEFT_PARENTHESIS
from celestine.unicode import RIGHT_PARENTHESIS
from celestine.unicode import ASTERISK
from celestine.unicode import PLUS_SIGN
from celestine.unicode import COMMA
from celestine.unicode import HYPHEN_MINUS
from celestine.unicode import FULL_STOP
from celestine.unicode import SOLIDUS
from celestine.unicode import DIGIT_ZERO
from celestine.unicode import DIGIT_ONE
from celestine.unicode import DIGIT_TWO
from celestine.unicode import DIGIT_THREE
from celestine.unicode import DIGIT_FOUR
from celestine.unicode import DIGIT_FIVE
from celestine.unicode import DIGIT_SIX
from celestine.unicode import DIGIT_SEVEN
from celestine.unicode import DIGIT_EIGHT
from celestine.unicode import DIGIT_NINE
from celestine.unicode import COLON
from celestine.unicode import SEMICOLON
from celestine.unicode import LESS_THAN_SIGN
from celestine.unicode import EQUALS_SIGN
from celestine.unicode import GREATER_THAN_SIGN
from celestine.unicode import QUESTION_MARK
from celestine.unicode import COMMERCIA_AT
from celestine.unicode import LATIN_CAPITAL_LETTER_A
from celestine.unicode import LATIN_CAPITAL_LETTER_B
from celestine.unicode import LATIN_CAPITAL_LETTER_C
from celestine.unicode import LATIN_CAPITAL_LETTER_D
from celestine.unicode import LATIN_CAPITAL_LETTER_E
from celestine.unicode import LATIN_CAPITAL_LETTER_F
from celestine.unicode import LATIN_CAPITAL_LETTER_G
from celestine.unicode import LATIN_CAPITAL_LETTER_H
from celestine.unicode import LATIN_CAPITAL_LETTER_I
from celestine.unicode import LATIN_CAPITAL_LETTER_J
from celestine.unicode import LATIN_CAPITAL_LETTER_K
from celestine.unicode import LATIN_CAPITAL_LETTER_L
from celestine.unicode import LATIN_CAPITAL_LETTER_M
from celestine.unicode import LATIN_CAPITAL_LETTER_N
from celestine.unicode import LATIN_CAPITAL_LETTER_O
from celestine.unicode import LATIN_CAPITAL_LETTER_P
from celestine.unicode import LATIN_CAPITAL_LETTER_Q
from celestine.unicode import LATIN_CAPITAL_LETTER_R
from celestine.unicode import LATIN_CAPITAL_LETTER_S
from celestine.unicode import LATIN_CAPITAL_LETTER_T
from celestine.unicode import LATIN_CAPITAL_LETTER_U
from celestine.unicode import LATIN_CAPITAL_LETTER_V
from celestine.unicode import LATIN_CAPITAL_LETTER_W
from celestine.unicode import LATIN_CAPITAL_LETTER_X
from celestine.unicode import LATIN_CAPITAL_LETTER_Y
from celestine.unicode import LATIN_CAPITAL_LETTER_Z
from celestine.unicode import LEFT_SQUARE_BRACKET
from celestine.unicode import REVERSE_SOLIDUS
from celestine.unicode import RIGHT_SQUARE_BRACKET
from celestine.unicode import CIRCUMFLEX_ACCENT
from celestine.unicode import LOW_LINE
from celestine.unicode import GRAVE_ACCENT
from celestine.unicode import LATIN_SMALL_LETTER_A
from celestine.unicode import LATIN_SMALL_LETTER_B
from celestine.unicode import LATIN_SMALL_LETTER_C
from celestine.unicode import LATIN_SMALL_LETTER_D
from celestine.unicode import LATIN_SMALL_LETTER_E
from celestine.unicode import LATIN_SMALL_LETTER_F
from celestine.unicode import LATIN_SMALL_LETTER_G
from celestine.unicode import LATIN_SMALL_LETTER_H
from celestine.unicode import LATIN_SMALL_LETTER_I
from celestine.unicode import LATIN_SMALL_LETTER_J
from celestine.unicode import LATIN_SMALL_LETTER_K
from celestine.unicode import LATIN_SMALL_LETTER_L
from celestine.unicode import LATIN_SMALL_LETTER_M
from celestine.unicode import LATIN_SMALL_LETTER_N
from celestine.unicode import LATIN_SMALL_LETTER_O
from celestine.unicode import LATIN_SMALL_LETTER_P
from celestine.unicode import LATIN_SMALL_LETTER_Q
from celestine.unicode import LATIN_SMALL_LETTER_R
from celestine.unicode import LATIN_SMALL_LETTER_S
from celestine.unicode import LATIN_SMALL_LETTER_T
from celestine.unicode import LATIN_SMALL_LETTER_U
from celestine.unicode import LATIN_SMALL_LETTER_V
from celestine.unicode import LATIN_SMALL_LETTER_W
from celestine.unicode import LATIN_SMALL_LETTER_X
from celestine.unicode import LATIN_SMALL_LETTER_Y
from celestine.unicode import LATIN_SMALL_LETTER_Z
from celestine.unicode import LEFT_CURLY_BRACKET
from celestine.unicode import VERTICAL_LINE
from celestine.unicode import RIGHT_CURLY_BRACKET
from celestine.unicode import TILDE
from celestine.unicode import DELETE
from celestine.unicode import U0080
from celestine.unicode import U0081
from celestine.unicode import BREAK_PERMITTED_HERE
from celestine.unicode import NO_BREAK_HERE
from celestine.unicode import INDEX
from celestine.unicode import NEXT_LINE
from celestine.unicode import START_OF_SELECTED_AREA
from celestine.unicode import END_OF_SELECTED_AREA
from celestine.unicode import CHARACTER_TABULATION_SET
from celestine.unicode import CHARACTER_TABULATION_WITHJUSTIFICATION
from celestine.unicode import LINE_TABULATION_SET
from celestine.unicode import PARTIAL_LINE_FORWARD
from celestine.unicode import PARTIAL_LINE_BACKWARD
from celestine.unicode import REVERSE_LINE_FEED
from celestine.unicode import SINGLE_SHIFT_TWO
from celestine.unicode import SINGLE_SHIFT_THREE
from celestine.unicode import DEVICE_CONTROL_STRING
from celestine.unicode import PRIVATE_USE_ONE
from celestine.unicode import PRIVATE_USE_TWO
from celestine.unicode import SET_TRANSMIT_STATE
from celestine.unicode import CANCEL_CHARACTER
from celestine.unicode import MESSAGE_WAITING
from celestine.unicode import START_OF_GUARDED_AREA
from celestine.unicode import END_OF_GUARDED_AREA
from celestine.unicode import START_OF_STRING
from celestine.unicode import U0099
from celestine.unicode import SINGLE_CHARACTER_INTRODUCER
from celestine.unicode import CONTROL_SEQUENCE_INTRODUCER
from celestine.unicode import STRING_TERMINATOR
from celestine.unicode import OPERATING_SYSTEM_COMMAND
from celestine.unicode import PRIVACY_MESSAGE
from celestine.unicode import APPLICATION_PROGRAM_COMMAND
from celestine.unicode import NO_BREAK_SPACE
from celestine.unicode import INVERTED_EXCLAMATION_MARK
from celestine.unicode import CENT_SIGN
from celestine.unicode import POUND_SIGN
from celestine.unicode import CURRENCY_SIGN
from celestine.unicode import YEN_SIGN
from celestine.unicode import BROKEN_BAR
from celestine.unicode import SECTION_SIGN
from celestine.unicode import DIAERESIS
from celestine.unicode import COPYRIGHT_SIGN
from celestine.unicode import FEMININE_ORDINAL_INDICATOR
from celestine.unicode import LEFT_POINTING_DOUBLE_ANGLE_QUOTATIONMARK
from celestine.unicode import NOT_SIGN
from celestine.unicode import SOFT_HYPHEN
from celestine.unicode import REGISTERED_SIGN
from celestine.unicode import MACRON
from celestine.unicode import DEGREE_SIGN
from celestine.unicode import PLUS_MINUS_SIGN
from celestine.unicode import SUPERSCRIPT_TWO
from celestine.unicode import SUPERSCRIPT_THREE
from celestine.unicode import ACUTE_ACCENT
from celestine.unicode import MICRO_SIGN
from celestine.unicode import PILCROW_SIGN
from celestine.unicode import MIDDLE_DOT
from celestine.unicode import CEDILLA
from celestine.unicode import SUPERSCRIPT_ONE
from celestine.unicode import MASCULINE_ORDINAL_INDICATOR
from celestine.unicode import RIGHT_POINTING_DOUBLE_ANGLE_QUOTATIONMARK
from celestine.unicode import VULGAR_FRACTION_ONE_QUARTER
from celestine.unicode import VULGAR_FRACTION_ONE_HALF
from celestine.unicode import VULGAR_FRACTION_THREE_QUARTERS
from celestine.unicode import INVERTED_QUESTION_MARK
from celestine.unicode import LATIN_CAPITAL_LETTER_A_WITH_GRAVE
from celestine.unicode import LATIN_CAPITAL_LETTER_A_WITH_ACUTE
from celestine.unicode import LATIN_CAPITAL_LETTER_A_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_CAPITAL_LETTER_A_WITH_TILDE
from celestine.unicode import LATIN_CAPITAL_LETTER_A_WITH_DIAERESIS
from celestine.unicode import LATIN_CAPITAL_LETTER_A_WITH_RING_ABOVE
from celestine.unicode import LATIN_CAPITAL_LETTER_AE
from celestine.unicode import LATIN_CAPITAL_LETTER_C_WITH_CEDILLA
from celestine.unicode import LATIN_CAPITAL_LETTER_E_WITH_GRAVE
from celestine.unicode import LATIN_CAPITAL_LETTER_E_WITH_ACUTE
from celestine.unicode import LATIN_CAPITAL_LETTER_E_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_CAPITAL_LETTER_E_WITH_DIAERESIS
from celestine.unicode import LATIN_CAPITAL_LETTER_I_WITH_GRAVE
from celestine.unicode import LATIN_CAPITAL_LETTER_I_WITH_ACUTE
from celestine.unicode import LATIN_CAPITAL_LETTER_I_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_CAPITAL_LETTER_I_WITH_DIAERESIS
from celestine.unicode import LATIN_CAPITAL_LETTER_ETH
from celestine.unicode import LATIN_CAPITAL_LETTER_N_WITH_TILDE
from celestine.unicode import LATIN_CAPITAL_LETTER_O_WITH_GRAVE
from celestine.unicode import LATIN_CAPITAL_LETTER_O_WITH_ACUTE
from celestine.unicode import LATIN_CAPITAL_LETTER_O_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_CAPITAL_LETTER_O_WITH_TILDE
from celestine.unicode import LATIN_CAPITAL_LETTER_O_WITH_DIAERESIS
from celestine.unicode import MULTIPLICATION_SIGN
from celestine.unicode import LATIN_CAPITAL_LETTER_O_WITH_STROKE
from celestine.unicode import LATIN_CAPITAL_LETTER_U_WITH_GRAVE
from celestine.unicode import LATIN_CAPITAL_LETTER_U_WITH_ACUTE
from celestine.unicode import LATIN_CAPITAL_LETTER_U_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_CAPITAL_LETTER_U_WITH_DIAERESIS
from celestine.unicode import LATIN_CAPITAL_LETTER_Y_WITH_ACUTE
from celestine.unicode import LATIN_CAPITAL_LETTER_THORN
from celestine.unicode import LATIN_SMALL_LETTER_SHARP_S
from celestine.unicode import LATIN_SMALL_LETTER_A_WITH_GRAVE
from celestine.unicode import LATIN_SMALL_LETTER_A_WITH_ACUTE
from celestine.unicode import LATIN_SMALL_LETTER_A_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_SMALL_LETTER_A_WITH_TILDE
from celestine.unicode import LATIN_SMALL_LETTER_A_WITH_DIAERESIS
from celestine.unicode import LATIN_SMALL_LETTER_A_WITH_RING_ABOVE
from celestine.unicode import LATIN_SMALL_LETTER_AE
from celestine.unicode import LATIN_SMALL_LETTER_C_WITH_CEDILLA
from celestine.unicode import LATIN_SMALL_LETTER_E_WITH_GRAVE
from celestine.unicode import LATIN_SMALL_LETTER_E_WITH_ACUTE
from celestine.unicode import LATIN_SMALL_LETTER_E_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_SMALL_LETTER_E_WITH_DIAERESIS
from celestine.unicode import LATIN_SMALL_LETTER_I_WITH_GRAVE
from celestine.unicode import LATIN_SMALL_LETTER_I_WITH_ACUTE
from celestine.unicode import LATIN_SMALL_LETTER_I_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_SMALL_LETTER_I_WITH_DIAERESIS
from celestine.unicode import LATIN_SMALL_LETTER_ETH
from celestine.unicode import LATIN_SMALL_LETTER_N_WITH_TILDE
from celestine.unicode import LATIN_SMALL_LETTER_O_WITH_GRAVE
from celestine.unicode import LATIN_SMALL_LETTER_O_WITH_ACUTE
from celestine.unicode import LATIN_SMALL_LETTER_O_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_SMALL_LETTER_O_WITH_TILDE
from celestine.unicode import LATIN_SMALL_LETTER_O_WITH_DIAERESIS
from celestine.unicode import DIVISION_SIGN
from celestine.unicode import LATIN_SMALL_LETTER_O_WITH_STROKE
from celestine.unicode import LATIN_SMALL_LETTER_U_WITH_GRAVE
from celestine.unicode import LATIN_SMALL_LETTER_U_WITH_ACUTE
from celestine.unicode import LATIN_SMALL_LETTER_U_WITH_CIRCUMFLEX
from celestine.unicode import LATIN_SMALL_LETTER_U_WITH_DIAERESIS
from celestine.unicode import LATIN_SMALL_LETTER_Y_WITH_ACUTE
from celestine.unicode import LATIN_SMALL_LETTER_THORN
from celestine.unicode import LATIN_SMALL_LETTER_Y_WITH_DIAERESIS
from celestine.unicode import BLACK_SAFETY_SCISSORS
from celestine.unicode import UPPER_BLADE_SCISSORS
from celestine.unicode import BLACK_SCISSORS
from celestine.unicode import LOWER_BLADE_SCISSORS
from celestine.unicode import WHITE_SCISSORS
from celestine.unicode import WHITE_HEAVY_CHECK_MARK
from celestine.unicode import TELEPHONE_LOCATION_SIGN
from celestine.unicode import TAPE_DRIVE
from celestine.unicode import AIRPLANE
from celestine.unicode import ENVELOPE
from celestine.unicode import RAISED_FIST
from celestine.unicode import RAISED_HAND
from celestine.unicode import VICTORY_HAND
from celestine.unicode import WRITING_HAND
from celestine.unicode import LOWER_RIGHT_PENCIL
from celestine.unicode import PENCIL
from celestine.unicode import UPPER_RIGHT_PENCIL
from celestine.unicode import WHITE_NIB
from celestine.unicode import BLACK_NIB
from celestine.unicode import CHECK_MARK
from celestine.unicode import HEAVY_CHECK_MARK
from celestine.unicode import MULTIPLICATION_X
from celestine.unicode import HEAVY_MULTIPLICATION_X
from celestine.unicode import BALLOT_X
from celestine.unicode import HEAVY_BALLOT_X
from celestine.unicode import OUTLINED_GREEK_CROSS
from celestine.unicode import HEAVY_GREEK_CROSS
from celestine.unicode import OPEN_CENTRE_CROSS
from celestine.unicode import HEAVY_OPEN_CENTRE_CROSS
from celestine.unicode import LATIN_CROSS
from celestine.unicode import SHADOWED_WHITE_LATIN_CROSS
from celestine.unicode import OUTLINED_LATIN_CROSS
from celestine.unicode import MALTESE_CROSS
from celestine.unicode import STAR_OF_DAVID
from celestine.unicode import FOUR_TEARDROP_SPOKED_ASTERISK
from celestine.unicode import FOUR_BALLOON_SPOKED_ASTERISK
from celestine.unicode import HEAVY_FOUR_BALLOON_SPOKED_ASTERISK
from celestine.unicode import FOUR_CLUB_SPOKED_ASTERISK
from celestine.unicode import BLACK_FOUR_POINTED_STAR
from celestine.unicode import WHITE_FOUR_POINTED_STAR
from celestine.unicode import SPARKLES
from celestine.unicode import STRESS_OUTLINED_WHITE_STAR
from celestine.unicode import CIRCLED_WHITE_STAR
from celestine.unicode import OPEN_CENTRE_BLACK_STAR
from celestine.unicode import BLACK_CENTRE_WHITE_STAR
from celestine.unicode import OUTLINED_BLACK_STAR
from celestine.unicode import HEAVY_OUTLINED_BLACK_STAR
from celestine.unicode import PINWHEEL_STAR
from celestine.unicode import SHADOWED_WHITE_STAR
from celestine.unicode import HEAVY_ASTERISK
from celestine.unicode import OPEN_CENTRE_ASTERISK
from celestine.unicode import EIGHT_SPOKED_ASTERISK
from celestine.unicode import EIGHT_POINTED_BLACK_STAR
from celestine.unicode import EIGHT_POINTED_PINWHEEL_STAR
from celestine.unicode import SIX_POINTED_BLACK_STAR
from celestine.unicode import EIGHT_POINTED_RECTILINEAR_BLACK_STAR
from celestine.unicode import HEAVY_EIGHT_POINTED_RECTILINEAR_BLACK_STAR
from celestine.unicode import TWELVE_POINTED_BLACK_STAR
from celestine.unicode import SIXTEEN_POINTED_ASTERISK
from celestine.unicode import TEARDROP_SPOKED_ASTERISK
from celestine.unicode import OPEN_CENTRE_TEARDROP_SPOKED_ASTERISK
from celestine.unicode import HEAVY_TEARDROP_SPOKED_ASTERISK
from celestine.unicode import SIX_PETALLED_BLACK_AND_WHITE_FLORETTE
from celestine.unicode import BLACK_FLORETTE
from celestine.unicode import WHITE_FLORETTE
from celestine.unicode import EIGHT_PETALLED_OUTLINED_BLACK_FLORETTE
from celestine.unicode import CIRCLED_OPEN_CENTRE_EIGHT_POINTED_STAR
from celestine.unicode import HEAVY_TEARDROP_SPOKED_PINWHEEL_ASTERISK
from celestine.unicode import SNOWFLAKE
from celestine.unicode import TIGHT_TRIFOLIATE_SNOWFLAKE
from celestine.unicode import HEAVY_CHEVRON_SNOWFLAKE
from celestine.unicode import SPARKLE
from celestine.unicode import HEAVY_SPARKLE
from celestine.unicode import BALLOON_SPOKED_ASTERISK
from celestine.unicode import EIGHT_TEARDROP_SPOKED_PROPELLER_ASTERISK
from celestine.unicode import HEAVY_EIGHT_TEARDROP_SPOKED_PROPELLER_ASTERISK
from celestine.unicode import CROSS_MARK
from celestine.unicode import SHADOWED_WHITE_CIRCLE
from celestine.unicode import NEGATIVE_SQUARED_CROSS_MARK
from celestine.unicode import LOWER_RIGHT_DROP_SHADOWED_WHITE_SQUARE
from celestine.unicode import UPPER_RIGHT_DROP_SHADOWED_WHITE_SQUARE
from celestine.unicode import LOWER_RIGHT_SHADOWED_WHITE_SQUARE
from celestine.unicode import UPPER_RIGHT_SHADOWED_WHITE_SQUARE
from celestine.unicode import BLACK_QUESTION_MARK_ORNAMENT
from celestine.unicode import WHITE_QUESTION_MARK_ORNAMENT
from celestine.unicode import WHITE_EXCLAMATION_MARK_ORNAMENT
from celestine.unicode import BLACK_DIAMOND_MINUS_WHITE_X
from celestine.unicode import HEAVY_EXCLAMATION_MARK_SYMBOL
from celestine.unicode import LIGHT_VERTICAL_BAR
from celestine.unicode import MEDIUM_VERTICAL_BAR
from celestine.unicode import HEAVY_VERTICAL_BAR
from celestine.unicode import HEAVY_SINGLE_TURNED_COMMA_QUOTATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_SINGLE_COMMA_QUOTATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_DOUBLE_TURNED_COMMA_QUOTATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_DOUBLE_COMMA_QUOTATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_LOW_SINGLE_COMMA_QUOTATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_LOW_DOUBLE_COMMA_QUOTATION_MARK_ORNAMENT
from celestine.unicode import CURVED_STEM_PARAGRAPH_SIGN_ORNAMENT
from celestine.unicode import HEAVY_EXCLAMATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_HEART_EXCLAMATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_BLACK_HEART
from celestine.unicode import ROTATED_HEAVY_BLACK_HEART_BULLET
from celestine.unicode import FLORAL_HEART
from celestine.unicode import ROTATED_FLORAL_HEART_BULLET
from celestine.unicode import MEDIUM_LEFT_PARENTHESIS_ORNAMENT
from celestine.unicode import MEDIUM_RIGHT_PARENTHESIS_ORNAMENT
from celestine.unicode import MEDIUM_FLATTENED_LEFT_PARENTHESIS_ORNAMENT
from celestine.unicode import MEDIUM_FLATTENED_RIGHT_PARENTHESIS_ORNAMENT
from celestine.unicode import MEDIUM_LEFT_POINTING_ANGLE_BRACKET_ORNAMENT
from celestine.unicode import MEDIUM_RIGHT_POINTING_ANGLE_BRACKET_ORNAMENT
from celestine.unicode import HEAVY_LEFT_POINTING_ANGLE_QUOTATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_RIGHT_POINTING_ANGLE_QUOTATION_MARK_ORNAMENT
from celestine.unicode import HEAVY_LEFT_POINTING_ANGLE_BRACKET_ORNAMENT
from celestine.unicode import HEAVY_RIGHT_POINTING_ANGLE_BRACKET_ORNAMENT
from celestine.unicode import LIGHT_LEFT_TORTOISE_SHELL_BRACKET_ORNAMENT
from celestine.unicode import LIGHT_RIGHT_TORTOISE_SHELL_BRACKET_ORNAMENT
from celestine.unicode import MEDIUM_LEFT_CURLY_BRACKET_ORNAMENT
from celestine.unicode import MEDIUM_RIGHT_CURLY_BRACKET_ORNAMENT
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_ONE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_TWO
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_THREE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_FOUR
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_FIVE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_SIX
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_SEVEN
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_EIGHT
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_DIGIT_NINE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_NUMBER_TEN
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_ONE
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_TWO
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_THREE
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_FOUR
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_FIVE
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_SIX
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_SEVEN
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_EIGHT
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_DIGIT_NINE
from celestine.unicode import DINGBAT_CIRCLED_SANS_SERIF_NUMBER_TEN
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_ONE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_TWO
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_THREE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_FOUR
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_FIVE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_SIX
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_SEVEN
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_EIGHT
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_NINE
from celestine.unicode import DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_NUMBER_TEN
from celestine.unicode import HEAVY_WIDE_HEADED_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_PLUS_SIGN
from celestine.unicode import HEAVY_MINUS_SIGN
from celestine.unicode import HEAVY_DIVISION_SIGN
from celestine.unicode import HEAVY_SOUTH_EAST_ARROW
from celestine.unicode import HEAVY_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_NORTH_EAST_ARROW
from celestine.unicode import DRAFTING_POINT_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_ROUND_TIPPED_RIGHTWARDS_ARROW
from celestine.unicode import TRIANGLE_HEADED_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_TRIANGLE_HEADED_RIGHTWARDS_ARROW
from celestine.unicode import DASHED_TRIANGLE_HEADED_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_DASHED_TRIANGLE_HEADED_RIGHTWARDS_ARROW
from celestine.unicode import BLACK_RIGHTWARDS_ARROW
from celestine.unicode import THREE_D_TOP_LIGHTED_RIGHTWARDS_ARROWHEAD
from celestine.unicode import THREE_D_BOTTOM_LIGHTED_RIGHTWARDS_ARROWHEAD
from celestine.unicode import BLACK_RIGHTWARDS_ARROWHEAD
from celestine.unicode import HEAVY_BLACK_CURVED_DOWNWARDS_AND_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_BLACK_CURVED_UPWARDS_AND_RIGHTWARDS_ARROW
from celestine.unicode import SQUAT_BLACK_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_CONCAVE_POINTED_BLACK_RIGHTWARDS_ARROW
from celestine.unicode import RIGHT_SHADED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import LEFT_SHADED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import BACK_TILTED_SHADOWED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import FRONT_TILTED_SHADOWED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_LOWER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_UPPER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import NOTCHED_LOWER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import CURLY_LOOP
from celestine.unicode import NOTCHED_UPPER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import CIRCLED_HEAVY_WHITE_RIGHTWARDS_ARROW
from celestine.unicode import WHITE_FEATHERED_RIGHTWARDS_ARROW
from celestine.unicode import BLACK_FEATHERED_SOUTH_EAST_ARROW
from celestine.unicode import BLACK_FEATHERED_RIGHTWARDS_ARROW
from celestine.unicode import BLACK_FEATHERED_NORTH_EAST_ARROW
from celestine.unicode import HEAVY_BLACK_FEATHERED_SOUTH_EAST_ARROW
from celestine.unicode import HEAVY_BLACK_FEATHERED_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_BLACK_FEATHERED_NORTH_EAST_ARROW
from celestine.unicode import TEARDROP_BARBED_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_TEARDROP_SHANKED_RIGHTWARDS_ARROW
from celestine.unicode import WEDGE_TAILED_RIGHTWARDS_ARROW
from celestine.unicode import HEAVY_WEDGE_TAILED_RIGHTWARDS_ARROW
from celestine.unicode import OPEN_OUTLINED_RIGHTWARDS_ARROW
from celestine.unicode import DOUBLE_CURLY_LOOP

from celestine.application.viewer.data.alphabet import Comparison
from celestine.application.viewer.data.alphabet import Digit
from celestine.application.viewer.data.alphabet import Divider
from celestine.application.viewer.data.alphabet import Letter
from celestine.application.viewer.data.alphabet import Unary


encoding = {
    NULL: True,
    START_OF_HEADING: Divider.WHITESPACE,
    START_OF_TEXT: Divider.WHITESPACE,
    END_OF_TEXT: Divider.WHITESPACE,
    END_OF_TRANSMISSION: Divider.WHITESPACE,
    ENQUIRY: Divider.WHITESPACE,
    ACKNOWLEDGE: Divider.WHITESPACE,
    BELL: Divider.WHITESPACE,
    BACKSPACE: Divider.WHITESPACE,
    CHARACTER_TABULATION: Divider.WHITESPACE,
    LINE_FEED: Divider.WHITESPACE,
    LINE_TABULATION: Divider.WHITESPACE,
    FORM_FEED: Divider.WHITESPACE,
    CARRIAGE_RETURN: Divider.WHITESPACE,
    SHIFT_OUT: Divider.WHITESPACE,
    SHIFT_IN: Divider.WHITESPACE,
    DATA_LINK_ESCAPE: Divider.WHITESPACE,
    DEVICE_CONTROL_ONE: Divider.WHITESPACE,
    DEVICE_CONTROL_TWO: Divider.WHITESPACE,
    DEVICE_CONTROL_THREE: Divider.WHITESPACE,
    DEVICE_CONTROL_FOUR: Divider.WHITESPACE,
    NEGATIVE_ACKNOWLEDGE: Divider.WHITESPACE,
    SYNCHRONOUS_IDLE: Divider.WHITESPACE,
    END_OF_TRANSMISSION_BLOCK: Divider.WHITESPACE,
    CANCEL: Divider.WHITESPACE,
    END_OF_MEDIUM: Divider.WHITESPACE,
    SUBSTITUTE: Divider.WHITESPACE,
    ESCAPE: Divider.WHITESPACE,
    INFORMATION_SEPARATOR_FOUR: Divider.WHITESPACE,
    INFORMATION_SEPARATOR_THREE: Divider.WHITESPACE,
    INFORMATION_SEPARATOR_TWO: Divider.WHITESPACE,
    INFORMATION_SEPARATOR_ONE: Divider.WHITESPACE,
    SPACE: Divider.WHITESPACE,
    EXCLAMATION_MARK: Comparison.MARK,
    QUOTATION_MARK: True,
    NUMBER_SIGN: True,
    DOLLAR_SIGN: True,
    PERCENT_SIGN: True,
    AMPERSAND: True,
    APOSTROPHE: True,
    LEFT_PARENTHESIS: True,
    RIGHT_PARENTHESIS: True,
    ASTERISK: Unary.STAR,
    PLUS_SIGN: Unary.PLUS,
    COMMA: True,
    HYPHEN_MINUS: Unary.DASH,
    FULL_STOP: True,
    SOLIDUS: True,
    DIGIT_ZERO: Digit.DIGIT_0,
    DIGIT_ONE: Digit.DIGIT_1,
    DIGIT_TWO: Digit.DIGIT_2,
    DIGIT_THREE: Digit.DIGIT_3,
    DIGIT_FOUR: Digit.DIGIT_4,
    DIGIT_FIVE: Digit.DIGIT_5,
    DIGIT_SIX: Digit.DIGIT_6,
    DIGIT_SEVEN: Digit.DIGIT_7,
    DIGIT_EIGHT: Digit.DIGIT_8,
    DIGIT_NINE: Digit.DIGIT_9,
    COLON: True,
    SEMICOLON: True,
    LESS_THAN_SIGN: Comparison.LESS,
    EQUALS_SIGN: Comparison.SAME,
    GREATER_THAN_SIGN: Comparison.MORE,
    QUESTION_MARK: True,
    COMMERCIA_AT: True,
    LATIN_CAPITAL_LETTER_A: Digit.DIGIT_A,
    LATIN_CAPITAL_LETTER_B: Digit.DIGIT_B,
    LATIN_CAPITAL_LETTER_C: Digit.DIGIT_C,
    LATIN_CAPITAL_LETTER_D: Digit.DIGIT_D,
    LATIN_CAPITAL_LETTER_E: Digit.DIGIT_E,
    LATIN_CAPITAL_LETTER_F: Digit.DIGIT_F,
    LATIN_CAPITAL_LETTER_G: True,
    LATIN_CAPITAL_LETTER_H: True,
    LATIN_CAPITAL_LETTER_I: True,
    LATIN_CAPITAL_LETTER_J: True,
    LATIN_CAPITAL_LETTER_K: True,
    LATIN_CAPITAL_LETTER_L: True,
    LATIN_CAPITAL_LETTER_M: True,
    LATIN_CAPITAL_LETTER_N: True,
    LATIN_CAPITAL_LETTER_O: True,
    LATIN_CAPITAL_LETTER_P: True,
    LATIN_CAPITAL_LETTER_Q: True,
    LATIN_CAPITAL_LETTER_R: True,
    LATIN_CAPITAL_LETTER_S: True,
    LATIN_CAPITAL_LETTER_T: True,
    LATIN_CAPITAL_LETTER_U: True,
    LATIN_CAPITAL_LETTER_V: True,
    LATIN_CAPITAL_LETTER_W: True,
    LATIN_CAPITAL_LETTER_X: True,
    LATIN_CAPITAL_LETTER_Y: True,
    LATIN_CAPITAL_LETTER_Z: True,
    LEFT_SQUARE_BRACKET: True,
    REVERSE_SOLIDUS: True,
    RIGHT_SQUARE_BRACKET: True,
    CIRCUMFLEX_ACCENT: True,
    LOW_LINE: Letter.LETTER__,
    GRAVE_ACCENT: True,
    LATIN_SMALL_LETTER_A: Letter.LETTER_A,
    LATIN_SMALL_LETTER_B: Letter.LETTER_B,
    LATIN_SMALL_LETTER_C: Letter.LETTER_C,
    LATIN_SMALL_LETTER_D: Letter.LETTER_D,
    LATIN_SMALL_LETTER_E: Letter.LETTER_E,
    LATIN_SMALL_LETTER_F: Letter.LETTER_F,
    LATIN_SMALL_LETTER_G: Letter.LETTER_G,
    LATIN_SMALL_LETTER_H: Letter.LETTER_H,
    LATIN_SMALL_LETTER_I: Letter.LETTER_I,
    LATIN_SMALL_LETTER_J: Letter.LETTER_J,
    LATIN_SMALL_LETTER_K: Letter.LETTER_K,
    LATIN_SMALL_LETTER_L: Letter.LETTER_L,
    LATIN_SMALL_LETTER_M: Letter.LETTER_M,
    LATIN_SMALL_LETTER_N: Letter.LETTER_N,
    LATIN_SMALL_LETTER_O: Letter.LETTER_O,
    LATIN_SMALL_LETTER_P: Letter.LETTER_P,
    LATIN_SMALL_LETTER_Q: Letter.LETTER_Q,
    LATIN_SMALL_LETTER_R: Letter.LETTER_R,
    LATIN_SMALL_LETTER_S: Letter.LETTER_S,
    LATIN_SMALL_LETTER_T: Letter.LETTER_T,
    LATIN_SMALL_LETTER_U: Letter.LETTER_U,
    LATIN_SMALL_LETTER_V: Letter.LETTER_V,
    LATIN_SMALL_LETTER_W: Letter.LETTER_W,
    LATIN_SMALL_LETTER_X: Letter.LETTER_X,
    LATIN_SMALL_LETTER_Y: Letter.LETTER_Y,
    LATIN_SMALL_LETTER_Z: Letter.LETTER_Z,
    LEFT_CURLY_BRACKET: True,
    VERTICAL_LINE: True,
    RIGHT_CURLY_BRACKET: True,
    TILDE: True,
    DELETE: True,
    U0080: True,
    U0081: True,
    BREAK_PERMITTED_HERE: True,
    NO_BREAK_HERE: True,
    INDEX: True,
    NEXT_LINE: True,
    START_OF_SELECTED_AREA: True,
    END_OF_SELECTED_AREA: True,
    CHARACTER_TABULATION_SET: True,
    CHARACTER_TABULATION_WITHJUSTIFICATION: True,
    LINE_TABULATION_SET: True,
    PARTIAL_LINE_FORWARD: True,
    PARTIAL_LINE_BACKWARD: True,
    REVERSE_LINE_FEED: True,
    SINGLE_SHIFT_TWO: True,
    SINGLE_SHIFT_THREE: True,
    DEVICE_CONTROL_STRING: True,
    PRIVATE_USE_ONE: True,
    PRIVATE_USE_TWO: True,
    SET_TRANSMIT_STATE: True,
    CANCEL_CHARACTER: True,
    MESSAGE_WAITING: True,
    START_OF_GUARDED_AREA: True,
    END_OF_GUARDED_AREA: True,
    START_OF_STRING: True,
    U0099: True,
    SINGLE_CHARACTER_INTRODUCER: True,
    CONTROL_SEQUENCE_INTRODUCER: True,
    STRING_TERMINATOR: True,
    OPERATING_SYSTEM_COMMAND: True,
    PRIVACY_MESSAGE: True,
    APPLICATION_PROGRAM_COMMAND: True,
    NO_BREAK_SPACE: Divider.WHITESPACE,
    INVERTED_EXCLAMATION_MARK: Comparison.MARK,
    CENT_SIGN: True,
    POUND_SIGN: True,
    CURRENCY_SIGN: True,
    YEN_SIGN: True,
    BROKEN_BAR: True,
    SECTION_SIGN: True,
    DIAERESIS: True,
    COPYRIGHT_SIGN: True,
    FEMININE_ORDINAL_INDICATOR: True,
    LEFT_POINTING_DOUBLE_ANGLE_QUOTATIONMARK: True,
    NOT_SIGN: True,
    SOFT_HYPHEN: Unary.DASH,
    REGISTERED_SIGN: True,
    MACRON: True,
    DEGREE_SIGN: True,
    PLUS_MINUS_SIGN: True,
    SUPERSCRIPT_TWO: True,
    SUPERSCRIPT_THREE: True,
    ACUTE_ACCENT: True,
    MICRO_SIGN: True,
    PILCROW_SIGN: True,
    MIDDLE_DOT: True,
    CEDILLA: True,
    SUPERSCRIPT_ONE: True,
    MASCULINE_ORDINAL_INDICATOR: True,
    RIGHT_POINTING_DOUBLE_ANGLE_QUOTATIONMARK: True,
    VULGAR_FRACTION_ONE_QUARTER: True,
    VULGAR_FRACTION_ONE_HALF: True,
    VULGAR_FRACTION_THREE_QUARTERS: True,
    INVERTED_QUESTION_MARK: True,
    LATIN_CAPITAL_LETTER_A_WITH_GRAVE: Letter.LETTER_A,
    LATIN_CAPITAL_LETTER_A_WITH_ACUTE: Letter.LETTER_A,
    LATIN_CAPITAL_LETTER_A_WITH_CIRCUMFLEX: Letter.LETTER_A,
    LATIN_CAPITAL_LETTER_A_WITH_TILDE: Letter.LETTER_A,
    LATIN_CAPITAL_LETTER_A_WITH_DIAERESIS: Letter.LETTER_A,
    LATIN_CAPITAL_LETTER_A_WITH_RING_ABOVE: Letter.LETTER_A,
    LATIN_CAPITAL_LETTER_AE: True,
    LATIN_CAPITAL_LETTER_C_WITH_CEDILLA: Letter.LETTER_C,
    LATIN_CAPITAL_LETTER_E_WITH_GRAVE: Letter.LETTER_E,
    LATIN_CAPITAL_LETTER_E_WITH_ACUTE: Letter.LETTER_E,
    LATIN_CAPITAL_LETTER_E_WITH_CIRCUMFLEX: Letter.LETTER_E,
    LATIN_CAPITAL_LETTER_E_WITH_DIAERESIS: Letter.LETTER_E,
    LATIN_CAPITAL_LETTER_I_WITH_GRAVE: Letter.LETTER_I,
    LATIN_CAPITAL_LETTER_I_WITH_ACUTE: Letter.LETTER_I,
    LATIN_CAPITAL_LETTER_I_WITH_CIRCUMFLEX: Letter.LETTER_I,
    LATIN_CAPITAL_LETTER_I_WITH_DIAERESIS: Letter.LETTER_I,
    LATIN_CAPITAL_LETTER_ETH: True,
    LATIN_CAPITAL_LETTER_N_WITH_TILDE: Letter.LETTER_N,
    LATIN_CAPITAL_LETTER_O_WITH_GRAVE: Letter.LETTER_O,
    LATIN_CAPITAL_LETTER_O_WITH_ACUTE: Letter.LETTER_O,
    LATIN_CAPITAL_LETTER_O_WITH_CIRCUMFLEX: Letter.LETTER_O,
    LATIN_CAPITAL_LETTER_O_WITH_TILDE: Letter.LETTER_O,
    LATIN_CAPITAL_LETTER_O_WITH_DIAERESIS: Letter.LETTER_O,
    MULTIPLICATION_SIGN: Unary.STAR,
    LATIN_CAPITAL_LETTER_O_WITH_STROKE: Letter.LETTER_O,
    LATIN_CAPITAL_LETTER_U_WITH_GRAVE: Letter.LETTER_U,
    LATIN_CAPITAL_LETTER_U_WITH_ACUTE: Letter.LETTER_U,
    LATIN_CAPITAL_LETTER_U_WITH_CIRCUMFLEX: Letter.LETTER_U,
    LATIN_CAPITAL_LETTER_U_WITH_DIAERESIS: Letter.LETTER_U,
    LATIN_CAPITAL_LETTER_Y_WITH_ACUTE: Letter.LETTER_Y,
    LATIN_CAPITAL_LETTER_THORN: True,
    LATIN_SMALL_LETTER_SHARP_S: True,
    LATIN_SMALL_LETTER_A_WITH_GRAVE: Letter.LETTER_A,
    LATIN_SMALL_LETTER_A_WITH_ACUTE: Letter.LETTER_A,
    LATIN_SMALL_LETTER_A_WITH_CIRCUMFLEX: Letter.LETTER_A,
    LATIN_SMALL_LETTER_A_WITH_TILDE: Letter.LETTER_A,
    LATIN_SMALL_LETTER_A_WITH_DIAERESIS: Letter.LETTER_A,
    LATIN_SMALL_LETTER_A_WITH_RING_ABOVE: Letter.LETTER_A,
    LATIN_SMALL_LETTER_AE: True,
    LATIN_SMALL_LETTER_C_WITH_CEDILLA: Letter.LETTER_C,
    LATIN_SMALL_LETTER_E_WITH_GRAVE: Letter.LETTER_E,
    LATIN_SMALL_LETTER_E_WITH_ACUTE: Letter.LETTER_E,
    LATIN_SMALL_LETTER_E_WITH_CIRCUMFLEX: Letter.LETTER_E,
    LATIN_SMALL_LETTER_E_WITH_DIAERESIS: Letter.LETTER_E,
    LATIN_SMALL_LETTER_I_WITH_GRAVE: Letter.LETTER_I,
    LATIN_SMALL_LETTER_I_WITH_ACUTE: Letter.LETTER_I,
    LATIN_SMALL_LETTER_I_WITH_CIRCUMFLEX: Letter.LETTER_I,
    LATIN_SMALL_LETTER_I_WITH_DIAERESIS: Letter.LETTER_I,
    LATIN_SMALL_LETTER_ETH: True,
    LATIN_SMALL_LETTER_N_WITH_TILDE: Letter.LETTER_N,
    LATIN_SMALL_LETTER_O_WITH_GRAVE: Letter.LETTER_O,
    LATIN_SMALL_LETTER_O_WITH_ACUTE: Letter.LETTER_O,
    LATIN_SMALL_LETTER_O_WITH_CIRCUMFLEX: Letter.LETTER_O,
    LATIN_SMALL_LETTER_O_WITH_TILDE: Letter.LETTER_O,
    LATIN_SMALL_LETTER_O_WITH_DIAERESIS: Letter.LETTER_O,
    DIVISION_SIGN: True,
    LATIN_SMALL_LETTER_O_WITH_STROKE: Letter.LETTER_O,
    LATIN_SMALL_LETTER_U_WITH_GRAVE: Letter.LETTER_U,
    LATIN_SMALL_LETTER_U_WITH_ACUTE: Letter.LETTER_U,
    LATIN_SMALL_LETTER_U_WITH_CIRCUMFLEX: Letter.LETTER_U,
    LATIN_SMALL_LETTER_U_WITH_DIAERESIS: Letter.LETTER_U,
    LATIN_SMALL_LETTER_Y_WITH_ACUTE: Letter.LETTER_Y,
    LATIN_SMALL_LETTER_THORN: True,
    LATIN_SMALL_LETTER_Y_WITH_DIAERESIS: Letter.LETTER_U,
    BLACK_SAFETY_SCISSORS: True,
    UPPER_BLADE_SCISSORS: True,
    BLACK_SCISSORS: True,
    LOWER_BLADE_SCISSORS: True,
    WHITE_SCISSORS: True,
    WHITE_HEAVY_CHECK_MARK: True,
    TELEPHONE_LOCATION_SIGN: True,
    TAPE_DRIVE: True,
    AIRPLANE: True,
    ENVELOPE: True,
    RAISED_FIST: True,
    RAISED_HAND: True,
    VICTORY_HAND: True,
    WRITING_HAND: True,
    LOWER_RIGHT_PENCIL: True,
    PENCIL: True,
    UPPER_RIGHT_PENCIL: True,
    WHITE_NIB: True,
    BLACK_NIB: True,
    CHECK_MARK: True,
    HEAVY_CHECK_MARK: True,
    MULTIPLICATION_X: Unary.STAR,
    HEAVY_MULTIPLICATION_X: Unary.STAR,
    BALLOT_X: True,
    HEAVY_BALLOT_X: True,
    OUTLINED_GREEK_CROSS: True,
    HEAVY_GREEK_CROSS: True,
    OPEN_CENTRE_CROSS: True,
    HEAVY_OPEN_CENTRE_CROSS: True,
    LATIN_CROSS: True,
    SHADOWED_WHITE_LATIN_CROSS: True,
    OUTLINED_LATIN_CROSS: True,
    MALTESE_CROSS: True,
    STAR_OF_DAVID: True,
    FOUR_TEARDROP_SPOKED_ASTERISK: True,
    FOUR_BALLOON_SPOKED_ASTERISK: True,
    HEAVY_FOUR_BALLOON_SPOKED_ASTERISK: True,
    FOUR_CLUB_SPOKED_ASTERISK: True,
    BLACK_FOUR_POINTED_STAR: True,
    WHITE_FOUR_POINTED_STAR: True,
    SPARKLES: True,
    STRESS_OUTLINED_WHITE_STAR: True,
    CIRCLED_WHITE_STAR: True,
    OPEN_CENTRE_BLACK_STAR: True,
    BLACK_CENTRE_WHITE_STAR: True,
    OUTLINED_BLACK_STAR: True,
    HEAVY_OUTLINED_BLACK_STAR: True,
    PINWHEEL_STAR: True,
    SHADOWED_WHITE_STAR: True,
    HEAVY_ASTERISK: True,
    OPEN_CENTRE_ASTERISK: True,
    EIGHT_SPOKED_ASTERISK: True,
    EIGHT_POINTED_BLACK_STAR: True,
    EIGHT_POINTED_PINWHEEL_STAR: True,
    SIX_POINTED_BLACK_STAR: True,
    EIGHT_POINTED_RECTILINEAR_BLACK_STAR: True,
    HEAVY_EIGHT_POINTED_RECTILINEAR_BLACK_STAR: True,
    TWELVE_POINTED_BLACK_STAR: True,
    SIXTEEN_POINTED_ASTERISK: True,
    TEARDROP_SPOKED_ASTERISK: True,
    OPEN_CENTRE_TEARDROP_SPOKED_ASTERISK: True,
    HEAVY_TEARDROP_SPOKED_ASTERISK: True,
    SIX_PETALLED_BLACK_AND_WHITE_FLORETTE: True,
    BLACK_FLORETTE: True,
    WHITE_FLORETTE: True,
    EIGHT_PETALLED_OUTLINED_BLACK_FLORETTE: True,
    CIRCLED_OPEN_CENTRE_EIGHT_POINTED_STAR: True,
    HEAVY_TEARDROP_SPOKED_PINWHEEL_ASTERISK: True,
    SNOWFLAKE: True,
    TIGHT_TRIFOLIATE_SNOWFLAKE: True,
    HEAVY_CHEVRON_SNOWFLAKE: True,
    SPARKLE: True,
    HEAVY_SPARKLE: True,
    BALLOON_SPOKED_ASTERISK: True,
    EIGHT_TEARDROP_SPOKED_PROPELLER_ASTERISK: True,
    HEAVY_EIGHT_TEARDROP_SPOKED_PROPELLER_ASTERISK: True,
    CROSS_MARK: Unary.STAR,
    SHADOWED_WHITE_CIRCLE: True,
    NEGATIVE_SQUARED_CROSS_MARK: True,
    LOWER_RIGHT_DROP_SHADOWED_WHITE_SQUARE: True,
    UPPER_RIGHT_DROP_SHADOWED_WHITE_SQUARE: True,
    LOWER_RIGHT_SHADOWED_WHITE_SQUARE: True,
    UPPER_RIGHT_SHADOWED_WHITE_SQUARE: True,
    BLACK_QUESTION_MARK_ORNAMENT: True,
    WHITE_QUESTION_MARK_ORNAMENT: True,
    WHITE_EXCLAMATION_MARK_ORNAMENT: Comparison.MARK,
    BLACK_DIAMOND_MINUS_WHITE_X: True,
    HEAVY_EXCLAMATION_MARK_SYMBOL: True,
    LIGHT_VERTICAL_BAR: True,
    MEDIUM_VERTICAL_BAR: True,
    HEAVY_VERTICAL_BAR: True,
    HEAVY_SINGLE_TURNED_COMMA_QUOTATION_MARK_ORNAMENT: True,
    HEAVY_SINGLE_COMMA_QUOTATION_MARK_ORNAMENT: True,
    HEAVY_DOUBLE_TURNED_COMMA_QUOTATION_MARK_ORNAMENT: True,
    HEAVY_DOUBLE_COMMA_QUOTATION_MARK_ORNAMENT: True,
    HEAVY_LOW_SINGLE_COMMA_QUOTATION_MARK_ORNAMENT: True,
    HEAVY_LOW_DOUBLE_COMMA_QUOTATION_MARK_ORNAMENT: True,
    CURVED_STEM_PARAGRAPH_SIGN_ORNAMENT: True,
    HEAVY_EXCLAMATION_MARK_ORNAMENT: Comparison.MARK,
    HEAVY_HEART_EXCLAMATION_MARK_ORNAMENT: Comparison.MARK,
    HEAVY_BLACK_HEART: True,
    ROTATED_HEAVY_BLACK_HEART_BULLET: True,
    FLORAL_HEART: True,
    ROTATED_FLORAL_HEART_BULLET: True,
    MEDIUM_LEFT_PARENTHESIS_ORNAMENT: True,
    MEDIUM_RIGHT_PARENTHESIS_ORNAMENT: True,
    MEDIUM_FLATTENED_LEFT_PARENTHESIS_ORNAMENT: True,
    MEDIUM_FLATTENED_RIGHT_PARENTHESIS_ORNAMENT: True,
    MEDIUM_LEFT_POINTING_ANGLE_BRACKET_ORNAMENT: Comparison.LESS,
    MEDIUM_RIGHT_POINTING_ANGLE_BRACKET_ORNAMENT: Comparison.MORE,
    HEAVY_LEFT_POINTING_ANGLE_QUOTATION_MARK_ORNAMENT: True,
    HEAVY_RIGHT_POINTING_ANGLE_QUOTATION_MARK_ORNAMENT: True,
    HEAVY_LEFT_POINTING_ANGLE_BRACKET_ORNAMENT: Comparison.LESS,
    HEAVY_RIGHT_POINTING_ANGLE_BRACKET_ORNAMENT: Comparison.MORE,
    LIGHT_LEFT_TORTOISE_SHELL_BRACKET_ORNAMENT: True,
    LIGHT_RIGHT_TORTOISE_SHELL_BRACKET_ORNAMENT: True,
    MEDIUM_LEFT_CURLY_BRACKET_ORNAMENT: True,
    MEDIUM_RIGHT_CURLY_BRACKET_ORNAMENT: True,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_ONE: Digit.DIGIT_1,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_TWO: Digit.DIGIT_2,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_THREE: Digit.DIGIT_3,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_FOUR: Digit.DIGIT_4,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_FIVE: Digit.DIGIT_5,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_SIX: Digit.DIGIT_6,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_SEVEN: Digit.DIGIT_7,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_EIGHT: Digit.DIGIT_8,
    DINGBAT_NEGATIVE_CIRCLED_DIGIT_NINE: Digit.DIGIT_9,
    DINGBAT_NEGATIVE_CIRCLED_NUMBER_TEN: Digit.DIGIT_A,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_ONE: Digit.DIGIT_1,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_TWO: Digit.DIGIT_2,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_THREE: Digit.DIGIT_3,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_FOUR: Digit.DIGIT_4,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_FIVE: Digit.DIGIT_5,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_SIX: Digit.DIGIT_6,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_SEVEN: Digit.DIGIT_7,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_EIGHT: Digit.DIGIT_8,
    DINGBAT_CIRCLED_SANS_SERIF_DIGIT_NINE: Digit.DIGIT_9,
    DINGBAT_CIRCLED_SANS_SERIF_NUMBER_TEN: Digit.DIGIT_A,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_ONE: Digit.DIGIT_1,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_TWO: Digit.DIGIT_2,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_THREE: Digit.DIGIT_3,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_FOUR: Digit.DIGIT_4,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_FIVE: Digit.DIGIT_5,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_SIX: Digit.DIGIT_6,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_SEVEN: Digit.DIGIT_7,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_EIGHT: Digit.DIGIT_8,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGIT_NINE: Digit.DIGIT_9,
    DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_NUMBER_TEN: Digit.DIGIT_A,
    HEAVY_WIDE_HEADED_RIGHTWARDS_ARROW: True,
    HEAVY_PLUS_SIGN: Unary.PLUS,
    HEAVY_MINUS_SIGN: Unary.DASH,
    HEAVY_DIVISION_SIGN: True,
    HEAVY_SOUTH_EAST_ARROW: True,
    HEAVY_RIGHTWARDS_ARROW: True,
    HEAVY_NORTH_EAST_ARROW: True,
    DRAFTING_POINT_RIGHTWARDS_ARROW: True,
    HEAVY_ROUND_TIPPED_RIGHTWARDS_ARROW: True,
    TRIANGLE_HEADED_RIGHTWARDS_ARROW: True,
    HEAVY_TRIANGLE_HEADED_RIGHTWARDS_ARROW: True,
    DASHED_TRIANGLE_HEADED_RIGHTWARDS_ARROW: True,
    HEAVY_DASHED_TRIANGLE_HEADED_RIGHTWARDS_ARROW: True,
    BLACK_RIGHTWARDS_ARROW: True,
    THREE_D_TOP_LIGHTED_RIGHTWARDS_ARROWHEAD: True,
    THREE_D_BOTTOM_LIGHTED_RIGHTWARDS_ARROWHEAD: True,
    BLACK_RIGHTWARDS_ARROWHEAD: True,
    HEAVY_BLACK_CURVED_DOWNWARDS_AND_RIGHTWARDS_ARROW: True,
    HEAVY_BLACK_CURVED_UPWARDS_AND_RIGHTWARDS_ARROW: True,
    SQUAT_BLACK_RIGHTWARDS_ARROW: True,
    HEAVY_CONCAVE_POINTED_BLACK_RIGHTWARDS_ARROW: True,
    RIGHT_SHADED_WHITE_RIGHTWARDS_ARROW: True,
    LEFT_SHADED_WHITE_RIGHTWARDS_ARROW: True,
    BACK_TILTED_SHADOWED_WHITE_RIGHTWARDS_ARROW: True,
    FRONT_TILTED_SHADOWED_WHITE_RIGHTWARDS_ARROW: True,
    HEAVY_LOWER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW: True,
    HEAVY_UPPER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW: True,
    NOTCHED_LOWER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW: True,
    CURLY_LOOP: True,
    NOTCHED_UPPER_RIGHT_SHADOWED_WHITE_RIGHTWARDS_ARROW: True,
    CIRCLED_HEAVY_WHITE_RIGHTWARDS_ARROW: True,
    WHITE_FEATHERED_RIGHTWARDS_ARROW: True,
    BLACK_FEATHERED_SOUTH_EAST_ARROW: True,
    BLACK_FEATHERED_RIGHTWARDS_ARROW: True,
    BLACK_FEATHERED_NORTH_EAST_ARROW: True,
    HEAVY_BLACK_FEATHERED_SOUTH_EAST_ARROW: True,
    HEAVY_BLACK_FEATHERED_RIGHTWARDS_ARROW: True,
    HEAVY_BLACK_FEATHERED_NORTH_EAST_ARROW: True,
    TEARDROP_BARBED_RIGHTWARDS_ARROW: True,
    HEAVY_TEARDROP_SHANKED_RIGHTWARDS_ARROW: True,
    WEDGE_TAILED_RIGHTWARDS_ARROW: True,
    HEAVY_WEDGE_TAILED_RIGHTWARDS_ARROW: True,
    OPEN_OUTLINED_RIGHTWARDS_ARROW: True,
    DOUBLE_CURLY_LOOP: True
}
