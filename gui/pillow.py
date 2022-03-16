from mem_dixy.module.python.os import OS
from mem_dixy.module.pillow.Image import Image
from mem_dixy.module.pillow.ImageDraw import ImageDraw
from mem_dixy.module.pillow.ImageFont import ImageFont

#import PIL.Image

class Array:
    @staticmethod
    def subdivide(array, subdivision_size):
        L = array
        S = subdivision_size
        print(array)
        print(len(range(S)))
        print(len(L))
        return [[L[a + b] for a in range(S)] for b in range(0, len(L), S)]


####
print("start")


class Style:
    def __del__(self):
        self.fill = None
        self.anchor = None
        self.spacing = None
        self.align = None
        self.stroke_width = None
        self.stroke_fill = None
        self.font = None
        self.size = None

    def __init__(self, font, size):
        self.fill = (255, 255, 255)
        self.anchor = "ma"
        self.spacing = 4
        self.align = "center"
        self.stroke_width = 0
        self.stroke_fill = (255, 255, 255)
        self.font = font
        self.size = size

    def truetype(self):
        return ImageFont.truetype(self.font, self.size)

    def text(self, x, y, text, ImageDraw):
        xy = (int(x), int(y))
        text = text
        fill = self.fill,
        font = self.truetype()
        anchor = self.anchor
        spacing = self.spacing
        align = self.align
        direction = None
        features = None
        language = None
        stroke_width = self.stroke_width
        stroke_fill = self.stroke_fill
        embedded_color = "SBIX"
        ImageDraw.text(xy, text, fill, font, anchor, spacing, align, direction, features, language, stroke_width, stroke_fill, embedded_color)


class Style2:
    def __del__(self):
        self.fill = None
        self.anchor = None
        self.spacing = None
        self.align = None
        self.stroke_width = None
        self.stroke_fill = None
        self.font = None
        self.size = None

    def __init__(self, font, size):
        self.fill = 255
        self.anchor = "ma"
        self.spacing = 4
        self.align = "center"
        self.stroke_width = 0
        self.stroke_fill = 255
        self.font = font
        self.size = size

    def truetype(self):
        return ImageFont.truetype(self.font, self.size)

    def text(self, x, y, text, ImageDraw):
        xy = (int(x), int(y))
        text = text
        fill = self.fill,
        font = self.truetype()
        anchor = self.anchor
        spacing = self.spacing
        align = self.align
        direction = None
        features = None
        language = None
        stroke_width = self.stroke_width
        stroke_fill = self.stroke_fill
        embedded_color = False
        ImageDraw.text(xy, text, fill, font, anchor, spacing, align, direction, features, language, stroke_width, stroke_fill, embedded_color)


class Canvas:
    def __del__(self):
        self.height = None
        self.ratio = None
        self.width = None

    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(round(x1))
        self.y1 = int(round(y1))
        self.x2 = int(round(x2))
        self.y2 = int(round(y2))
        self.height = self.y2 - self.y1
        self.width = self.x2 - self.x1
        self.ratio = self.width / self.height

    @classmethod
    def scale(cls, canvas, x, y):
        width = canvas.width * x
        height = canvas.height * y
        offset_x = (canvas.width - width) / 2
        offset_y = (canvas.height - height) / 2
        return cls(offset_x, offset_y, offset_x + width, offset_y + height)


JPG_QUALITY = 100
#
screen = Canvas(0, 0, 3840, 2160)
screen = Canvas(0, 0, 1920 * 4, 1080 * 4)
action_safe = Canvas.scale(screen, 0.93, 0.93)
title_safe = Canvas.scale(screen, 0.80, 0.90)
#
picture = Canvas(0, 0, screen.width, screen.width / 2)
caption = Canvas(title_safe.x1, picture.height, title_safe.x2, screen.height)
text = Canvas(0, 0, caption.width, caption.height / 3)
#
page = Canvas(0, 0, screen.height * 8.5 / 11, screen.height)
page_left = Canvas(0, 0, page.width, page.height)
page_right = Canvas(screen.width / 2, 0, page.width, page.height)


paths = [
    ("28_BLACK_16_01.png", "", "", ""),
    ("60_BLACK_18_06.png", "", "", ""),
    ("23_NEGATIVE_027-BLACK_17_01.png", "", "", ""),
    ("06_NEGATIVE_244.png", "", "", ""),
    ("26_NEGATIVE_569.png", "", "", ""),
    ("42_BLACK_26_03.png", "", "", ""),
    ("18_BLACK_11_02.png", "", "", ""),
    ("55_NEGATIVE_488.png", "", "", ""),
    ("10_NEGATIVE_212.png", "", "", ""),
    ("57_NEGATIVE_214-BLACK_18_01.png", "", "", ""),
    ("31_NEGATIVE_549.png", "", "", ""),
    ("12_BLACK_25_08.png", "", "", ""),
    ("25_RED_34_05.png", "", "", ""),
    ("17_NEGATIVE_354.png", "", "", ""),
    ("36_NEGATIVE_433.png", "", "", ""),
    ("08_BLACK_19_04.png", "", "", ""),
    ("30_NEGATIVE_098.png", "", "", ""),
    ("61_NEGATIVE_576.png", "", "", ""),
    ("22_NEGATIVE_551.png", "", "", ""),
    ("02_BLACK_28_03.png", "", "", ""),
    ("26_RED_34_01.png", "", "", ""),
    ("05a_NEGATIVE_186.png", "", "", ""),
    ("17_NEGATIVE_382.png", "", "", ""),
    ("18_NEGATIVE_232.png", "", "", ""),
    ("27_NEGATIVE_536.png", "", "", ""),
    ("09_NEGATIVE_188-BLACK_25_01.png", "", "", ""),
    ("13_BLACK_28_04.png", "", "", ""),
    ("51_NEGATIVE_300.png", "", "", ""),
    ("47_NEGATIVE_587.png", "", "", ""),
    ("15_RED_22_02.png", "", "", ""),
    ("05_BLACK_02_01.png", "", "", ""),
    ("07_BLACK_07_05.png", "", "", ""),
    ("47_BLACK_15_01.png", "", "", ""),
    ("25_NEGATIVE_548.png", "", "", ""),
    ("23_BLACK_09_01.png", "", "", ""),
    ("33_NEGATIVE_456.png", "", "", ""),
    ("07_RED_01_07.png", "", "", ""),
    ("02_BLACK_24_01.png", "", "", ""),
    ("28_NEGATIVE_533.png", "", "", ""),
    ("33_BLACK_25_06.png", "", "", ""),
    ("19_NEGATIVE_291.png", "", "", ""),
    ("18_NEGATIVE_556.png", "", "", ""),
    ("35_NEGATIVE_107-BLACK_30_05.png", "", "", ""),
    ("02_NEGATIVE_055.png", "", "", ""),
    ("52_NEGATIVE_526.png", "", "", ""),
    ("26_NEGATIVE_387.png", "", "", ""),
    ("16_BLACK_07_02.png", "", "", ""),
    ("39_NEGATIVE_351.png", "", "", ""),
    ("10_NEGATIVE_039-RED_34_02.png", "", "", ""),
    ("59_NEGATIVE_159-BLACK_17_04.png", "", "", ""),
    ("06_RED_04_05.png", "", "", ""),
    ("49_NEGATIVE_494.png", "", "", ""),
    ("07_NEGATIVE_153.png", "", "", ""),
    ("34_NEGATIVE_464.png", "", "", ""),
    ("08_NEGATIVE_196.png", "", "", ""),
    ("14_NEGATIVE_412.png", "", "", ""),
    ("42_NEGATIVE_290.png", "", "", ""),
    ("20_NEGATIVE_507.png", "", "", ""),
    ("01_NEGATIVE_260.png", "", "", ""),
    ("04_RED_03_06.png", "", "", ""),
    ("15_NEGATIVE_048.png", "", "", ""),
    ("09_BLACK_25_03.png", "", "", ""),
    ("07_NEGATIVE_224.png", "", "", ""),
    ("02_NEGATIVE_125-BLACK_32_04.png", "", "", ""),
    ("15_BLACK_20_02.png", "", "", ""),
    ("32_NEGATIVE_435.png", "", "", ""),
    ("32_NEGATIVE_199-BLACK_12_02.png", "", "", ""),
    ("38_RED_18_05.png", "", "", ""),
    ("24_BLACK_09_04.png", "", "", ""),
    ("49_NEGATIVE_522.png", "", "", ""),
    ("14_NEGATIVE_238.png", "", "", ""),
    ("21_BLACK_02_05.png", "", "", ""),
    ("50_NEGATIVE_156-BLACK_14_04.png", "", "", ""),
    ("13_NEGATIVE_356.png", "", "", ""),
    ("65_NEGATIVE_560.png", "", "", ""),
    ("13_NEGATIVE_183.png", "", "", ""),
    ("36_NEGATIVE_227.png", "", "", ""),
    ("07_NEGATIVE_208.png", "", "", ""),
    ("26_NEGATIVE_553.png", "", "", ""),
    ("04_RED_29_06.png", "", "", ""),
    ("37_NEGATIVE_443.png", "", "", ""),
    ("38_NEGATIVE_444.png", "", "", ""),
    ("06_NEGATIVE_322.png", "", "", ""),
    ("03_NEGATIVE_010-RED_33_07.png", "", "", ""),
    ("36_NEGATIVE_421.png", "", "", ""),
    ("03_RED_01_03.png", "", "", ""),
    ("17_BLACK_01_03.png", "", "", ""),
    ("66_NEGATIVE_620.png", "", "", ""),
    ("14_BLACK_02_03.png", "", "", ""),
    ("29_NEGATIVE_434.png", "", "", ""),
    ("04_NEGATIVE_410.png", "", "", ""),
    ("18_BLACK_03_04.png", "", "", ""),
    ("29_NEGATIVE_623.png", "", "", ""),
    ("15_NEGATIVE_461.png", "", "", ""),
    ("18_BLACK_03_05.png", "", "", ""),
    ("20_NEGATIVE_099.png", "", "", ""),
    ("11_BLACK_31_03.png", "", "", ""),
    ("01_NEGATIVE_271.png", "", "", ""),
    ("17_NEGATIVE_347.png", "", "", ""),
    ("13_BLACK_02_06.png", "", "", ""),
    ("38_NEGATIVE_451.png", "", "", ""),
    ("46_NEGATIVE_130.png", "", "", ""),
    ("12_NEGATIVE_066-RED_34_03.png", "", "", ""),
    ("10_BLACK_27_02.png", "", "", ""),
    ("13_NEGATIVE_141.png", "", "", ""),
    ("16_RED_22_01.png", "", "", ""),
    ("30_NEGATIVE_198-BLACK_11_04.png", "", "", ""),
    ("56_BLACK_19_02.png", "", "", ""),
    ("10_BLACK_03_03.png", "", "", ""),
    ("12_RED_20_05.png", "", "", ""),
    ("15_BLACK_30_02.png", "", "", ""),
    ("22_RED_24_03.png", "", "", ""),
    ("07_NEGATIVE_004-BLACK_21_03.png", "", "", ""),
    ("56_NEGATIVE_530.png", "", "", ""),
    ("25_NEGATIVE_228.png", "", "", ""),
    ("46_NEGATIVE_287.png", "", "", ""),
    ("04_RED_01_04.png", "", "", ""),
    ("00_RED_13_05.png", "", "", ""),
    ("17_RED_25_04.png", "", "", ""),
    ("11_RED_20_02.png", "", "", ""),
    ("03_NEGATIVE_151.png", "", "", ""),
    ("17_NEGATIVE_392.png", "", "", ""),
    ("24_NEGATIVE_369-BLACK_32_01.png", "", "", ""),
    ("04_NEGATIVE_163.png", "", "", ""),
    ("38_NEGATIVE_071-BLACK_17_03.png", "", "", ""),
    ("32_NEGATIVE_547.png", "", "", ""),
    ("24_NEGATIVE_303.png", "", "", ""),
    ("22_NEGATIVE_541.png", "", "", ""),
    ("41_NEGATIVE_288.png", "", "", ""),
    ("08_NEGATIVE_379.png", "", "", ""),
    ("29_NEGATIVE_378.png", "", "", ""),
    ("27_NEGATIVE_195-BLACK_13_03.png", "", "", ""),
    ("22_NEGATIVE_025-BLACK_09_03.png", "", "", ""),
    ("49_NEGATIVE_312-BLACK_14_03.png", "", "", ""),
    ("19_NEGATIVE_321.png", "", "", ""),
    ("09_RED_05_02.png", "", "", ""),
    ("12_BLACK_06_04.png", "", "", ""),
    ("08_NEGATIVE_225.png", "", "", ""),
    ("20_NEGATIVE_313.png", "", "", ""),
    ("03_RED_03_04.png", "", "", ""),
    ("45_NEGATIVE_298.png", "", "", ""),
    ("10_BLACK_25_04.png", "", "", ""),
    ("NEGATIVE_084.png", "", "", ""),
    ("28_NEGATIVE_087.png", "", "", ""),
    ("NEGATIVE_245.png", "", "", ""),
    ("58_NEGATIVE_568.png", "", "", ""),
    ("23_NEGATIVE_319.png", "", "", ""),
    ("40_RED_17_01.png", "", "", ""),
    ("06_RED_08_02.png", "", "", ""),
    ("22_NEGATIVE_026-BLACK_16_06.png", "", "", ""),
    ("04_BLACK_04_02.png", "", "", ""),
    ("32_NEGATIVE_396.png", "", "", ""),
    ("56_NEGATIVE_542.png", "", "", ""),
    ("09_BLACK_17_07.png", "", "", ""),
    ("05_NEGATIVE_007.png", "", "", ""),
    ("03_BLACK_26_01.png", "", "", ""),
    ("16_NEGATIVE_355.png", "", "", ""),
    ("43_NEGATIVE_293.png", "", "", ""),
    ("54_NEGATIVE_489.png", "", "", ""),
    ("11_NEGATIVE_213.png", "", "", ""),
    ("23_NEGATIVE_550.png", "", "", ""),
    ("40_NEGATIVE_299.png", "", "", ""),
    ("16_NEGATIVE_202-BLACK_10_02.png", "", "", ""),
    ("11_BLACK_03_02.png", "", "", ""),
    ("14_NEGATIVE_124-BLACK_32_05.png", "", "", ""),
    ("05_NEGATIVE_402.png", "", "", ""),
    ("34_NEGATIVE_439.png", "", "", ""),
    ("12_NEGATIVE_218.png", "", "", ""),
    ("NEGATIVE_394.png", "", "", ""),
    ("47_NEGATIVE_490.png", "", "", ""),
    ("08_RED_04_02.png", "", "", ""),
    ("01_RED_02_01.png", "", "", ""),
    ("25_NEGATIVE_008_BLACK_09_06.png", "", "", ""),
    ("25_NEGATIVE_028-BLACK_17_05.png", "", "", ""),
    ("09_NEGATIVE_427.png", "", "", ""),
    ("04_NEGATIVE_006-BLACK_20_03.png", "", "", ""),
    ("06_BLACK_07_01.png", "", "", ""),
    ("01_BLACK_23_04.png", "", "", ""),
    ("03_BLACK_28_05.png", "", "", ""),
    ("08_RED_30_06.png", "", "", ""),
    ("53_NEGATIVE_486.png", "", "", ""),
    ("19_NEGATIVE_233.png", "", "", ""),
    ("32_RED_32_06.png", "", "", ""),
    ("36_RED_16_06.png", "", "", ""),
    ("06_BLACK_33_05.png", "", "", ""),
    ("22_NEGATIVE_309.png", "", "", ""),
    ("17_RED_07_03.png", "", "", ""),
    ("16_NEGATIVE_036.png", "", "", ""),
    ("52_NEGATIVE_168-BLACK_18_04.png", "", "", ""),
    ("07_RED_40_04.png", "", "", ""),
    ("19_RED_13_06.png", "", "", ""),
    ("54_NEGATIVE_529.png", "", "", ""),
    ("28_NEGATIVE_544.png", "", "", ""),
    ("18_NEGATIVE_284.png", "", "", ""),
    ("41_BLACK_17_06.png", "", "", ""),
    ("12_NEGATIVE_193.png", "", "", ""),
    ("43_NEGATIVE_455.png", "", "", ""),
    ("27_NEGATIVE_580.png", "", "", ""),
    ("29_BLACK_16_04.png", "", "", ""),
    ("05_BLACK_04_03.png", "", "", ""),
    ("11_NEGATIVE_078-BLACK_34_09.png", "", "", ""),
    ("04_BLACK_02_07.png", "", "", ""),
    ("16_NEGATIVE_381.png", "", "", ""),
    ("27_NEGATIVE_033-BLACK_09_05.png", "", "", ""),
    ("37_NEGATIVE_380.png", "", "", ""),
    ("36_NEGATIVE_447.png", "", "", ""),
    ("11_BLACK_25_05.png", "", "", ""),
    ("21_BLACK_32_03.png", "", "", ""),
    ("47_NEGATIVE_450.png", "", "", ""),
    ("15_NEGATIVE_413.png", "", "", ""),
    ("02_RED_23_22.png", "", "", ""),
    ("17_NEGATIVE_121-BLACK_35_07.png", "", "", ""),
    ("46_NEGATIVE_432.png", "", "", ""),
    ("24_NEGATIVE_072-BLACK_16_08.png", "", "", ""),
    ("07_RED_09_01.png", "", "", ""),
    ("41_RED_16_02.png", "", "", ""),
    ("17_BLACK_33_01.png", "", "", ""),
    ("13_RED_21_05.png", "", "", ""),
    ("14_RED_21_01.png", "", "", ""),
    ("21_NEGATIVE_314.png", "", "", ""),
    ("16_BLACK_01_01.png", "", "", ""),
    ("08_BLACK_01_04.png", "", "", ""),
    ("12_NEGATIVE_409.png", "", "", ""),
    ("31_NEGATIVE_100.png", "", "", ""),
    ("16_BLACK_27_01.png", "", "", ""),
    ("15_NEGATIVE_239.png", "", "", ""),
    ("26_NEGATIVE_068.png", "", "", ""),
    ("23_RED_37_07.png", "", "", ""),
    ("06_NEGATIVE_209.png", "", "", ""),
    ("09_NEGATIVE_226.png", "", "", ""),
    ("27_NEGATIVE_234.png", "", "", ""),
    ("19_NEGATIVE_552.png", "", "", ""),
    ("21_NEGATIVE_310.png", "", "", ""),
    ("37_BLACK_14_01.png", "", "", ""),
    ("18_RED_22_05.png", "", "", ""),
    ("12_NEGATIVE_182.png", "", "", ""),
    ("01_RED_24_02.png", "", "", ""),
    ("NEGATIVE_185.png", "", "", ""),
    ("37_NEGATIVE_420.png", "", "", ""),
    ("27_NEGATIVE_426.png", "", "", ""),
    ("43_RED_27_05.png", "", "", ""),
    ("06_BLACK_07_06.png", "", "", ""),
    ("11_RED_10_02.png", "", "", ""),
    ("07_RED_31_01.png", "", "", ""),
    ("15_BLACK_26_04.png", "", "", ""),
    ("12_NEGATIVE_237.png", "", "", ""),
    ("03_BLACK_34_07.png", "", "", ""),
    ("05_NEGATIVE_411.png", "", "", ""),
    ("60_NEGATIVE_565.png", "", "", ""),
    ("09_NEGATIVE_192.png", "", "", ""),
    ("04_NEGATIVE_472.png", "", "", ""),
    ("16_NEGATIVE_144_.png", "", "", ""),
    ("48_NEGATIVE_491.png", "", "", ""),
    ("15_BLACK_10_04.png", "", "", ""),
    ("18_BLACK_09_07.png", "", "", ""),
    ("28_NEGATIVE_385.png", "", "", ""),
    ("03_NEGATIVE_093.png", "", "", ""),
    ("36_BLACK_12_04.png", "", "", ""),
    ("03_NEGATIVE_118.png", "", "", ""),
    ("04_NEGATIVE_062.png", "", "", ""),
    ("02_BLACK_06_06.png", "", "", ""),
    ("13_NEGATIVE_023-RED_35_03.png", "", "", ""),
    ("13_BLACK_25_09.png", "", "", ""),
    ("11_BLACK_27_04.png", "", "", ""),
    ("20_NEGATIVE_035-RED_36_03.png", "", "", ""),
    ("23_NEGATIVE_384.png", "", "", ""),
    ("28_NEGATIVE_230.png", "", "", ""),
    ("23_RED_27_01.png", "", "", ""),
    ("61_BLACK_18_05.png", "", "", ""),
    ("63_NEGATIVE_578.png", "", "", ""),
    ("01_RED_24_01.png", "", "", ""),
    ("03_RED_40_03.png", "", "", ""),
    ("12_RED_10_04.png", "", "", ""),
    ("16_RED_23_20.png", "", "", ""),
    ("41_NEGATIVE_229.png", "", "", ""),
    ("01_BLACK_31_01.png", "", "", ""),
    ("10_NEGATIVE_077.png", "", "", ""),
    ("15_NEGATIVE_102-BLACK_06_02.png", "", "", ""),
    ("08_BLACK_03_07.png", "", "", ""),
    ("13_NEGATIVE_110-BLACK_35_01.png", "", "", ""),
    ("03_RED_15_03.png", "", "", ""),
    ("18_NEGATIVE_320.png", "", "", ""),
    ("13_RED_21_03.png", "", "", ""),
    ("39_RED_17_03.png", "", "", ""),
    ("10_RED_19_02.png", "", "", ""),
    ("03_BLACK_02_04.png", "", "", ""),
    ("64_NEGATIVE_577.png", "", "", ""),
    ("05_NEGATIVE_085-BLACK_33_04.png", "", "", ""),
    ("10_NEGATIVE_473.png", "", "", ""),
    ("06_NEGATIVE_223.png", "", "", ""),
    ("10_NEGATIVE_117.png", "", "", ""),
    ("06_NEGATIVE_009.png", "", "", ""),
    ("35_NEGATIVE_270.png", "", "", ""),
    ("48_BLACK_14_02.png", "", "", ""),
    ("11_BLACK_06_07.png", "", "", ""),
    ("01_NEGATIVE_618.png", "", "", ""),
    ("19_RED_22_04.png", "", "", ""),
    ("58_NEGATIVE_174-BLACK_15_04.png", "", "", ""),
    ("05_BLACK_01_05.png", "", "", ""),
    ("44_NEGATIVE_294.png", "", "", ""),
    ("06_NEGATIVE_414.png", "", "", ""),
    ("02_RED_40_01.png", "", "", ""),
    ("29_NEGATIVE_470.png", "", "", ""),
    ("25_RED_29_02.png", "", "", ""),
    ("42_RED_27_04.png", "", "", ""),
    ("38_NEGATIVE_164.png", "", "", ""),
    ("13_BLACK_01_06.png", "", "", ""),
    ("23_BLACK_30_04.png", "", "", ""),
    ("48_NEGATIVE_448.png", "", "", ""),
    ("51_BLACK_18_02.png", "", "", ""),
    ("03_NEGATIVE_275.png", "", "", ""),
    ("01_NEGATIVE_037.png", "", "", ""),
    ("35_NEGATIVE_446.png", "", "", ""),
    ("24_RED_30_04.png", "", "", ""),
    ("19_NEGATIVE_126-BLACK_35_09.png", "", "", ""),
    ("20_BLACK_05_04.png", "", "", ""),
    ("27_NEGATIVE_400.png", "", "", ""),
    ("05_NEGATIVE_184.png", "", "", ""),
    ("40_NEGATIVE_069-BLACK_16_03.png", "", "", ""),
    ("11_NEGATIVE_063-RED_33_04.png", "", "", ""),
    ("41_NEGATIVE_422.png", "", "", ""),
    ("11_NEGATIVE_145.png", "", "", ""),
    ("20_NEGATIVE_181.png", "", "", ""),
    ("59_NEGATIVE_559.png", "", "", ""),
    ("35_NEGATIVE_177-BLACK_12_01.png", "", "", ""),
    ("27_NEGATIVE_088-BLACK_30_08.png", "", "", ""),
    ("01_BLACK_34_03.png", "", "", ""),
    ("06_NEGATIVE_211.png", "", "", ""),
    ("33_RED_32_03.png", "", "", ""),
    ("12_NEGATIVE_169-BLACK_28_01.png", "", "", ""),
    ("01_RED_07_06.png", "", "", ""),
    ("18_BLACK_26_02.png", "", "", ""),
    ("44_NEGATIVE_452.png", "", "", ""),
    ("34_NEGATIVE_172-BLACK_12_03.png", "", "", ""),
    ("15_NEGATIVE_143.png", "", "", ""),
    ("06_BLACK_28_02.png", "", "", ""),
    ("33_BLACK_12_05.png", "", "", ""),
    ("11_NEGATIVE_219.png", "", "", ""),
    ("NEGATIVE_162.png", "", "", ""),
    ("21_NEGATIVE_283.png", "", "", ""),
    ("26_RED_29_04.png", "", "", ""),
    ("04_NEGATIVE_325.png", "", "", ""),
    ("50_NEGATIVE_524.png", "", "", ""),
    ("09_RED_22_03.png", "", "", ""),
    ("45_NEGATIVE_154.png", "", "", ""),
    ("18_NEGATIVE_111.png", "", "", ""),
    ("43_NEGATIVE_307.png", "", "", ""),
    ("32_BLACK_30_01.png", "", "", ""),
    ("22_NEGATIVE_317.png", "", "", ""),
    ("08_NEGATIVE_108-BLACK_34_02.png", "", "", ""),
    ("25_NEGATIVE_537.png", "", "", ""),
    ("16_BLACK_20_05.png", "", "", ""),
    ("07_RED_34_04.png", "", "", ""),
    ("06_NEGATIVE_002.png", "", "", ""),
    ("14_BLACK_03_01.png", "", "", ""),
    ("12_BLACK_02_08.png", "", "", ""),
    ("05_NEGATIVE_222.png", "", "", ""),
    ("14_NEGATIVE_044.png", "", "", ""),
    ("44_NEGATIVE_286.png", "", "", ""),
    ("14_BLACK_13_04.png", "", "", ""),
    ("07_NEGATIVE_276.png", "", "", ""),
    ("26_NEGATIVE_539.png", "", "", ""),
    ("05_BLACK_29_02.png", "", "", ""),
    ("05_NEGATIVE_020.png", "", "", ""),
    ("10_RED_10_05.png", "", "", ""),
    ("15_RED_23_13.png", "", "", ""),
    ("09_NEGATIVE_401.png", "", "", ""),
    ("34_RED_32_02.png", "", "", ""),
    ("20_NEGATIVE_555.png", "", "", ""),
    ("08_NEGATIVE_477.png", "", "", ""),
    ("17_NEGATIVE_462.png", "", "", ""),
    ("04_BLACK_33_02.png", "", "", ""),
    ("17_NEGATIVE_064-RED_35_06.png", "", "", ""),
    ("07_BLACK_18_03.png", "", "", ""),
    ("34_BLACK_24_04.png", "", "", ""),
    ("02_NEGATIVE_205.png", "", "", ""),
    ("08_BLACK_04_04.png", "", "", ""),
    ("17_RED_24_10.png", "", "", ""),
    ("25_NEGATIVE_368-BLACK_30_07.png", "", "", ""),
    ("28_NEGATIVE_429.png", "", "", ""),
    ("38_NEGATIVE_349.png", "", "", ""),
    ("14_NEGATIVE_086.png", "", "", ""),
    ("04_NEGATIVE_094.png", "", "", ""),
    ("10_BLACK_10_01.png", "", "", ""),
    ("12_BLACK_34_08.png", "", "", ""),
    ("02_NEGATIVE_173.png", "", "", ""),
    ("30_NEGATIVE_397.png", "", "", ""),
    ("07_BLACK_04_06.png", "", "", ""),
    ("19_NEGATIVE_200.png", "", "", ""),
    ("05_RED_05_06.png", "", "", ""),
    ("55_BLACK_19_05.png", "", "", ""),
    ("33_NEGATIVE_438.png", "", "", ""),
    ("22_RED_37_01.png", "", "", ""),
    ("14_BLACK_25_10.png", "", "", ""),
    ("06_RED_40_07.png", "", "", ""),
    ("46_NEGATIVE_210.png", "", "", ""),
    ("44_RED_16_01.png", "", "", ""),
    ("02_NEGATIVE_398.png", "", "", ""),
    ("22_NEGATIVE_304.png", "", "", ""),
    ("24_NEGATIVE_546.png", "", "", ""),
    ("50_NEGATIVE_495.png", "", "", ""),
    ("16_BLACK_08_03.png", "", "", ""),
    ("13_NEGATIVE_471.png", "", "", ""),
    ("18_NEGATIVE_274.png", "", "", ""),
    ("30_NEGATIVE_430.png", "", "", ""),
    ("28_NEGATIVE_403.png", "", "", ""),
    ("53_NEGATIVE_528.png", "", "", ""),
    ("24_NEGATIVE_383.png", "", "", ""),
    ("37_NEGATIVE_166.png", "", "", ""),
    ("21_BLACK_13_01.png", "", "", ""),
    ("18_BLACK_36_01.png", "", "", ""),
    ("21_NEGATIVE_024-BLACK_09_08.png", "", "", ""),
    ("15_NEGATIVE_353.png", "", "", ""),
    ("10_BLACK_02_02.png", "", "", ""),
    ("35_NEGATIVE_457.png", "", "", ""),
    ("14_NEGATIVE_318.png", "", "", ""),
    ("13_BLACK_29_03.png", "", "", ""),
    ("17_BLACK_24_02.png", "", "", ""),
    ("09_NEGATIVE_167.png", "", "", ""),
    ("29_NEGATIVE_306.png", "", "", ""),
    ("11_NEGATIVE_236.png", "", "", ""),
    ("31_BLACK_31_02.png", "", "", ""),
    ("29_BLACK_11_03.png", "", "", ""),
    ("09_NEGATIVE_106-BLACK_06_08.png", "", "", ""),
    ("02_NEGATIVE_170.png", "", "", ""),
    ("18_NEGATIVE_046-RED_35_05.png", "", "", ""),
    ("02_RED_07_04.png", "", "", ""),
    ("04_NEGATIVE_242.png", "", "", ""),
    ("37_RED_18_01.png", "", "", ""),
    ("10_NEGATIVE_179.png", "", "", ""),
    ("01_NEGATIVE_090-BLACK_30_06.png", "", "", ""),
    ("04_BLACK_03_06.png", "", "", ""),
    ("03_NEGATIVE_405.png", "", "", ""),
    ("35_RED_33_01.png", "", "", ""),
    ("20_NEGATIVE_091-BLACK_30_03.png", "", "", ""),
    ("16_NEGATIVE_263.png", "", "", ""),
    ("19_RED_36_06.png", "", "", ""),
    ("39_NEGATIVE_029-BLACK_16_09.png", "", "", ""),
    ("45_NEGATIVE_295.png", "", "", ""),
    ("02_RED_01_02.png", "", "", ""),
    ("10_BLACK_06_01.png", "", "", ""),
    ("05_RED_03_03.png", "", "", ""),
    ("15_NEGATIVE_123.png", "", "", ""),
    ("62_NEGATIVE_575.png", "", "", ""),
    ("16_NEGATIVE_129.png", "", "", ""),
    ("07_NEGATIVE_171.png", "", "", ""),
    ("21_RED_36_08.png", "", "", ""),
    ("24_NEGATIVE_441.png", "", "", ""),
    ("25_NEGATIVE_386.png", "", "", ""),
    ("24_NEGATIVE_469.png", "", "", ""),
    ("14_RED_06_04.png", "", "", ""),
    ("03_RED_30_05.png", "", "", ""),
    ("19_NEGATIVE_197-BLACK_08_01 (1942).png", "", "", ""),
    ("30_BLACK_05_05.png", "", "", ""),
    ("39_NEGATIVE_428.png", "", "", ""),
    ("NEGATIVE_393-BLACK_17_02.png", "", "", ""),
    ("09_BLACK_01_08.png", "", "", ""),
    ("21_RED_24_09.png", "", "", ""),
    ("55_NEGATIVE_523.png", "", "", ""),
    ("22_NEGATIVE_149.png", "", "", ""),
    ("40_NEGATIVE_437.png", "", "", ""),
    ("01_BLACK_06_05.png", "", "", ""),
    ("33_NEGATIVE_463.png", "", "", ""),
    ("10_NEGATIVE_191.png", "", "", ""),
    ("01_BLACK_20_01.png", "", "", ""),
    ("52_NEGATIVE_301.png", "", "", ""),
    ("05_RED_01_05.png", "", "", ""),
    ("08_NEGATIVE_203.png", "", "", ""),
    ("14_NEGATIVE_142.png", "", "", ""),
    ("16_NEGATIVE_466.png", "", "", ""),
    ("39_NEGATIVE_416.png", "", "", ""),
    ("53_BLACK_19_03.png", "", "", ""),
    ("45_NEGATIVE_453.png", "", "", ""),
    ("19_NEGATIVE_139.png", "", "", ""),
    ("41_NEGATIVE_292.png", "", "", ""),
    ("04_BLACK_29_01.png", "", "", ""),
    ("51_NEGATIVE_525.png", "", "", ""),
    ("08_NEGATIVE_161.png", "", "", ""),
    ("54_BLACK_19_06.png", "", "", ""),
    ("45_RED_31_05.png", "", "", ""),
    ("20_NEGATIVE_308.png", "", "", ""),
    ("31_NEGATIVE_436.png", "", "", ""),
    ("09_BLACK_04_07.png", "", "", ""),
    ("02_NEGATIVE_115.png", "", "", ""),
    ("11_NEGATIVE_119.png", "", "", ""),
    ("57_NEGATIVE_574.png", "", "", ""),
    ("13_NEGATIVE_415.png", "", "", ""),
    ("31_NEGATIVE_152.png", "", "", ""),
    ("23_NEGATIVE_302.png", "", "", ""),
    ("14_NEGATIVE_235.png", "", "", ""),
    ("46_NEGATIVE_500.png", "", "", ""),
    ("19_NEGATIVE_074.png", "", "", ""),
    ("20_RED_12_01.png", "", "", ""),
    ("01_NEGATIVE_133.png", "", "", ""),
    ("11_NEGATIVE_647.png", "", "", ""),
    ("02_RED_03_01.png", "", "", ""),
    ("08_NEGATIVE_104-BLACK_07_07.png", "", "", ""),
    ("15_BLACK_01_02.png", "", "", ""),
    ("21_NEGATIVE_554.png", "", "", ""),
    ("21_NEGATIVE_540.png", "", "", ""),
    ("26_NEGATIVE_406.png", "", "", ""),
    ("14_NEGATIVE_190.png", "", "", ""),
    ("20_NEGATIVE_278.png", "", "", ""),
    ("06_BLACK_04_01.png", "", "", ""),
    ("27_RED_12_05.png", "", "", ""),
    ("30_NEGATIVE_083.png", "", "", ""),
    ("12_RED_25_01.png", "", "", ""),
    ("NEGATIVE_460.png", "", "", ""),
    ("34_NEGATIVE_454.png", "", "", ""),
    ("01_RED_01_01.png", "", "", ""),
    ("02_NEGATIVE_272.png", "", "", ""),
    ("02_BLACK_07_04.png", "", "", ""),
    ("12_BLACK_01_07.png", "", "", ""),
    ("42_NEGATIVE_459.png", "", "", ""),
    ("19_NEGATIVE_277.png", "", "", ""),
    ("42_NEGATIVE_465.png", "", "", ""),
    ("13_NEGATIVE_089-BLACK_07_03.png", "", "", ""),
    ("07_NEGATIVE_022-BLACK_05_02.png", "", "", ""),
    ("08_NEGATIVE_011.png", "", "", ""),
    ("40_NEGATIVE_419.png", "", "", ""),
    ("25_NEGATIVE_545.png", "", "", ""),
    ("03_NEGATIVE_399.png", "", "", ""),
    ("23_NEGATIVE_305.png", "", "", ""),
    ("06_RED_01_06.png", "", "", ""),
    ("09_BLACK_35_08.png", "", "", ""),
    ("07_NEGATIVE_079-BLACK_34_05.png", "", "", ""),
    ("44_NEGATIVE_231.png", "", "", ""),
    ("05_NEGATIVE_097.png", "", "", ""),
    ("26_NEGATIVE_032-BLACK_09_02.png", "", "", ""),
    ("09_RED_02_03.png", "", "", ""),
    ("40_NEGATIVE_194.png", "", "", ""),
    ("23_NEGATIVE_070-BLACK_16_07.png", "", "", ""),
    ("17_NEGATIVE_204.png", "", "", ""),
    ("01_RED_39_06.png", "", "", ""),
    ("22_NEGATIVE_096-BLACK_30_09.png", "", "", ""),
    ("07_NEGATIVE_404.png", "", "", ""),
    ("39_NEGATIVE_160.png", "", "", ""),
    ("05_NEGATIVE_323.png", "", "", ""),
    ("17_BLACK_08_04.png", "", "", ""),
    ("26_BLACK_31_07.png", "", "", ""),
    ("05_NEGATIVE_135.png", "", "", ""),
    ("24_RED_34_06.png", "", "", ""),
    ("31_NEGATIVE_395.png", "", "", ""),
    ("20_BLACK_35_02.png", "", "", ""),
    ("43_NEGATIVE_389.png", "", "", ""),
    ("03_BLACK_25_02.png", "", "", ""),
    ("04_NEGATIVE_221.png", "", "", "")
]

paths = [
    ("Control_Screenshot_2.jpg", "Phil in his military uniform", "November 1944", ""),
    ("Control_Screenshot_3.jpg", "Phil in his military uniform", "November 1944", "")
]

# ("A.jpg", "1234567890!@#$%^&*()_+=-[]}{;':./?>,<QWzxZXOILPyY", "1234567890!@#$%^&*()_+=-[]}{;':./?>,<QWzxZXOILPyY", "1234567890!@#$%^&*()_+=-[]}{;':./?>,<QWzxZXOILPyY"),


def convert_to_jpg(array):
    global screen
    global text

    (name, text_0, text_1, text_2) = array
    path = OS.join("todo", name)
    print("convert " + path)

    photo = Image.open(path)

    mode = "L" if photo.image.mode == "L" else "RGB"

    image = Image.new("RGB", screen.width, screen.height)

    #style = Style("/System/Library/Fonts/HelveticaNeue.ttc", 64)
    #style = Style("/System/Library/Fonts/Supplemental/AmericanTypewriter.ttc", 128)
    print("C:\Windows\Fonts\Arial.ttf")
    style = Style("C:\Windows\Fonts\Arial.ttf", 128)
    

    line = [item for item in [text_0, text_1, text_2] if item != ""]
    lines = len(line)

    picture = Canvas(0, 0, screen.width, screen.height - (text.height * lines))
    new_width = picture.width
    new_height = picture.height
    if photo.ratio >= picture.ratio:
        new_height = round(picture.width / photo.ratio)
    else:
        new_width = round(picture.height * photo.ratio)
    photo.resize(new_width, new_height)
    offx = (picture.width - new_width) / 2
    offy = (picture.height - new_height) / 2

    image.paste(photo, offx, offy)
    draw = ImageDraw.Draw(image.image)

    if lines == 0:
        pass
    if lines == 1:
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[0], draw)
    if lines == 2:
        style.text(screen.width / 2, caption.y1 + (text.height * 1), line[0], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[1], draw)
    if lines == 3:
        style.text(screen.width / 2, caption.y1 + (text.height * 0), line[0], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 1), line[1], draw)
        style.text(screen.width / 2, caption.y1 + (text.height * 2), line[2], draw)

    image.convert(mode)

    new_name = OS.join("done", name)
    names = new_name.split(".")
    image_save = names[0] + ".jpg"
    print("saved " + image_save)
    image.save_jpg(image_save)


def make_dvd(left, right):
    name1 = OS.join("todo", left)
    name2 = OS.join("todo", right)
    print("convert " + name1)
    print("convert " + name2)
    background = Image.new("RGB", screen.width, screen.height)

    image_left = Image.open(name1)
    image_left.resize_to_height(screen.height)

    image_right = Image.open(name2)
    image_right.resize_to_height(screen.height)

    screen_middle = screen.width / 2
    background.paste(image_left, screen_middle - image_left.width, 0)
    background.paste(image_right, screen_middle, 0)

    new_name = OS.join("done", left)
    names = new_name.split(".")
    image_save = names[0] + ".jpg"
    print("saved " + image_save)
    background.save_jpg(image_save)


def main(array):
    for item in array:
        convert_to_jpg(item)


def dvd(array):
    for item in Array.subdivide(array, 2):
        left = item[0]
        right = item[1]
        make_dvd(left, right)


print("finish")


# https://help.fontlab.com/fontlab/7/manual/Color-Font-Formats/


print("scan")


def load_paths():
    (path, file) = OS.chdir("todo", OS.walk_directory)
    OS.chdir("done", OS.makedirs, path)
    array = []
    for (item) in file:
        root = "todo"
        (name, path) = item
        array.append(name)
    return array


def jpg_quality_test(path):
    image_open = OS.join("todo", path)
    image = Image.open(image_open)
    for quality in range(101):
        name = str(quality) + ".jpg"
        image_save = OS.join("done", name)
        print("saved " + image_save)
        image.save_jpg(image_save, quality)


main(paths)
paths = load_paths()
paths.sort()
# paths.remove(".DS_Store")
for item in paths:
    print(item + ",")

dvd(paths)

# jpg_quality_test(paths[0])


print("done")


# /System/Library/Fonts/Supplemental/Arial\ Unicode.ttf
# /System/Library/Fonts/Supplemental/AmericanTypewriter.ttc

