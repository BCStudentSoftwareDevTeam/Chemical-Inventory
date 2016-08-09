window.conversionObject = {
    master: {
        "Mass/Weight": {
            "gram (g)": "1",
            "kilogram (kg)": "0.001",
            "pound (lb)": "2.20462262e-3",
        },
        "Temperature": {
            "Celsius": "1",
            "Kelvin": "1",
            "Fahrenheit": "1",
            "Rankine": "1"
        },
        "Volume": {
            "ounce (oz)": "33814.02220161",
            "gallon (gal)": "264.17205124",
            "liter (L)": "1000",
            "milliliter (mL)": "1e+6",
        }
    },

    functions: {
        converter: function (context, from, to, subject) {
            subject = parseInt(subject);
            var specialTest = false;
            for (var i in window.conversionObject.special) {
                if (i == context) {
                    specialTest = i;
                }
            }
            if (specialTest !== false) {
                if (typeof window.conversionObject.special[specialTest][from] !== "undefined") {
                    return window.conversionObject.special[specialTest][from]["to" + to](subject);
                }
                return false;
            }
            return window.conversionObject.master[context][to] / window.conversionObject.master[context][from] * subject;
        }
    }
}