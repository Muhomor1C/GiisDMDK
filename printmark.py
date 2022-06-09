import ctypes


def printmark(name, weight_full, weight_metall, uin, barcode):
    tsclibrary = ctypes.WinDLL(".//libs//TSCLIB.dll")
    tsclibrary.openportW("USB")
    tsclibrary.sendcommandW("SIZE 30 mm, 22 mm")
    tsclibrary.sendcommandW("DIRECTION 1")
    tsclibrary.sendcommandW("CLS")
    tsclibrary.windowsfontW(
            "130",
            "145",
            "18",
            "90",
            "0",
            "0",
            "Arial",
            name,
        )  # 15 symbols
    tsclibrary.windowsfontW(
                "160",
                "145",
                "16",
                "90",
                "0",
                "0",
                "Arial",
                "Вес изделия: "+weight_full,
            )
    tsclibrary.windowsfontW(
               "175",
               "145",
               "16",
               "90",
               "0",
               "0",
               "Arial",
               "Вес металла: "+weight_metall,
        )  # 17

    tsclibrary.barcodeW(
               "195",
               "120",
               "EAN13",
               "40",
               "0",
               "270",
               "1",
               "1",
               barcode
    )

    tsclibrary.sendcommandW(f"TEXT 110, 7, \"1\", 90, 0, 0, \"{uin}\"")
    tsclibrary.sendcommandW(f"DMATRIX 25, 42, 120, 120, \"{uin}\"")
    tsclibrary.sendcommandW("DIAGONAL 120, 0, 120, 145, 5")
    tsclibrary.sendcommandW("PRINT 1, 1")
    tsclibrary.closeport()


if __name__ == "__main__":
    printmark("Sssssssssssssssfffffddd", "0.25", "0.2", 1234567890123456, str(1234567890123))
