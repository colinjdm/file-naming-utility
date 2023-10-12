
/* Mouseover tooltip that follows the mouse as it moves */

function tooltip(elementId) {
    var element = document.getElementById(elementId);
    /* Master ID */
    if (element.id === "header1") {
        var tooltip = document.getElementById('tooltip1');
        tooltip.innerText = "Master ID is a 3 to 5 digit number.";
    }
    /* Permit Number */
    if (element.id === "header2") {
        var tooltip = document.getElementById('tooltip2');
        tooltip.innerText = "Permit numbers can vary. Hazardous Waste permits are typically 12 digits and often begin with ALD.";
    }
    /* County Code */
    if (element.id === "header3") {
        var tooltip = document.getElementById('tooltip3');
        tooltip.innerText = "County codes are 3 digits.";
    }
    /* Date */
    if (element.id === "header4") {
        var tooltip = document.getElementById('tooltip4');
        tooltip.innerText = "Date the document was received by ADEM (MM-DD-YYYY).";
    }
    /* Type */
    if (element.id === "header5") {
        var tooltip = document.getElementById('tooltip5');
        tooltip.innerText = "Four-letter document type code.";
    }
    /* Initials */
    if (element.id === "header6") {
        var tooltip = document.getElementById('tooltip6');
        tooltip.innerText = "Your intials.";
    }
    /* Title */
    if (element.id === "header7") {
        var tooltip = document.getElementById('tooltip7');
        tooltip.innerText = "Title of the document.  Must be less than 64 characters.";
    }
    /* Shows the tooltip on mouseover */
    element.onmousemove = function(event) {
        this.style.color = "#B2533E";
        tooltip.style.display = 'block';
        /* Tooltip offset, in pixels */
        tooltip.style.left = (event.clientX + 10) + 'px';
        tooltip.style.top = (event.clientY + 10) + 'px';
    }
    /* Hides the tooltip on mouseout */
    element.onmouseout = function() {
        this.style.color = "white";
        tooltip.style.display = 'none';

    }
}
