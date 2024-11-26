// Encapsulate code to prevent polluting the global scope
(function () {
    document.addEventListener("DOMContentLoaded", function () {
        const container = document.getElementById('spreadsheet');

        const data = [
            ['Operation', 'Value B', 'Value C', 'Result'],
            ['Addition: Total Pocket Money', 15, 20, '=B2+C2'],
            ['Subtraction: Money leftover from Shopping', 35, 10, '=B3-C3'],
            ['Multiplication (value * quantity)', 10, 5, '=B4*C4'],
            ['Division (quantity / value)', 10, 5, '=B5/C5'],
        ];

        // Create a new instance of HyperFormula (used by Handsontable for formulas)
        const hyperFormulaInstance = HyperFormula.buildEmpty({
            licenseKey: 'non-commercial-and-evaluation'
        });

        // Initialie Handsontable with the defined data and settings
        const hot = new Handsontable(container, {
            data: data,
            rowHeaders: true,
            colHeaders: true,
            contextMenu: true,
            formulas: {
                engine: hyperFormulaInstance
            },
            height: 'auto',
            licenseKey: 'non-commercial-and-evaluation',
            cells: function (row, col) {
                const cellProperties = {};

                return cellProperties;
            }
        });
    });
})();
