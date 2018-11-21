function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                alert(allText);
            }
        }
    }
    rawFile.send(null);
}


function xml()
{
	var parser, xmlDoc;
	var text = readTextFile(\runmate_project\static\GPX\Lugano.gpx);
	parser = new DOMParser();
	xmlDoc = parser.parseFromString(text, "text/xml");

	document.getElementById("gpx").innerHTML = xmlDoc.getElementsByTagName("trkpt lat")[0].childNodes[0].nodeValue;
}