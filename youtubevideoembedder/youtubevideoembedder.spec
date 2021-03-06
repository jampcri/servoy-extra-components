{
	"name": "servoyextra-youtubevideoembedder",
	"displayName": "Embedded YouTube",
	"version": 1,
	"definition": "servoyextra/youtubevideoembedder/youtubevideoembedder.js",
	"libraries": [{ "name": "servoyextra-youtubeembed-css", "version": "1.0", "url": "servoyextra/youtubevideoembedder/youtubevideoembedder.css", "mimetype": "text/css" }],
    "icon": "servoyextra/youtubevideoembedder/youtubevideoembedder.png",
	"model": {
        "embeddedVideoURL": { "type": "string" },
	
		"videoWidth": { "type": "int", "default": 426 },
		"videoHeight": { "type": "int", "default": 240 },
		"allowFullScreen": { "type": "boolean", "default": true },
		"autoPlay": { "type": "boolean", "default": false },
		"showControls": { "type": "boolean", "default": true },
		"modestBranding": { "type": "boolean", "default": false },
		"showRelatedVideosAtEnd": { "type": "boolean", "default": false },
		
        "styleClass": { "type" :"styleclass", "default": "youtubevideoembedder" }, 
        "tabSeq": { "type" :"tabseq", "tags": { "scope": "design" } }, 
        "visible": "visible",
        
        "size" : {"type": "dimension", "default": { "width": 426, "height": 240 }, "pushToServer": "deep"}
	}
}