# QConvert Demo

## Install

Clone this repository, and then run:

```bash
npm install
```

## Start

```bash
npm start
```

Program will scan `./input/` directory for `.json` files, and will convert each `.json` to Qiskit and SVG. See `index.js` file on how to add more export formats. JSON files are Quantastica's internal format for storing quantum circuits. Files can be imported and exported from/to quantum-circuit.js using `.load()` and `.save()` methods. Format is also supported by [Quantum Programming Studio](https://quantum-circuit.com) (both import and export).


## Development

If you are adding new features to [quantum-circuit.js](https://www.npmjs.com/package/quantum-circuit) package, install your local version of quantum-circuit which you cloned from [https://github.com/quantastica/quantum-circuit](https://github.com/quantastica/quantum-circuit):

```bash
npm remove quantum-circuit
npm install "local directory where you cloned quantum-circuit"
```


### Enjoy! :)
