#!/usr/bin/node
const { argv } = require("node:process");
argv.length > 1 ? console.log("Arguments found") : console.log("No argument");
