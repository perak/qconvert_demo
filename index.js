const fs = require("fs");
const path = require("path");
const QuantumCircuit = require("quantum-circuit");

function changeFileExt(filePath, newExtension) {
	const parsedPath = path.parse(filePath);
	const newFilePath = path.format({
		...parsedPath,
		base: undefined, // Remove base to let ext and name take precedence
		ext: newExtension.startsWith('.') ? newExtension : `.${newExtension}`,
	});

	return newFilePath;
}

// Function to list all JSON files in the given directory
function listJsonFiles(directory) {
	let jsonFiles = [];
	try {
		const files = fs.readdirSync(directory); // Read all files in the directory
		const tempList = files.filter(file => path.extname(file).toLowerCase() === '.json'); // Filter JSON files

		tempList.map(function(filename) {
			jsonFiles.push({ directory: directory, filename: filename, path: path.join(directory, filename) });
		});
	} catch (err) {
		console.error(`Error reading directory: ${err.message}`);
	}

	return jsonFiles;
}

function convertCode(inputDir, outputDir, outputFormat) {
	if(!outputFormat) {
		throw new Error("Output format is not specified.");
	}

	const jsonFiles = listJsonFiles(inputDir);

	const outputPath = path.resolve(path.join(outputDir, outputFormat));
	fs.mkdirSync(outputPath, { recursive: true });

	jsonFiles.map((jsonFile) => {
		console.log("Exporting \"" + jsonFile.path + "\" to \"" + outputFormat + "\"...");

		const obj = JSON.parse(fs.readFileSync(jsonFile.path));

		const qc = new QuantumCircuit();
		qc.load(obj);

		var outputContent = "";
		var fileExt = "";
		switch(outputFormat) {
			case "qiskit": {
				outputContent = qc.exportToQiskit();
				fileExt = ".py";
			}; break;
			case "svg": {
				outputContent = qc.exportToSVG();
				fileExt = ".svg";
			}; break;
			// case "cudaq": {
			//	 outputContent = qc.exportToCudaQ();
			//	 fileExt = ".py";
			// }; break;

			default: {
				console.error(`Unknown format "${outputFormat}".`);
			}
		}

		const outputFilename = changeFileExt(jsonFile.filename, fileExt);

		const outputFilePath = path.join(outputPath, outputFilename);
		fs.writeFileSync(outputFilePath, outputContent);			
		console.log("Output is written to \"" + outputFilePath + "\".\n");
	});
	console.log("Done.\n");
}

convertCode("input", "output", "qiskit");
convertCode("input", "output", "svg");
// convertCode("./input/", "./output/", "cudaq");
