const mongoose = require("mongoose");

const availablePostSchema = new mongoose.Schema({
    id: { type: String, required: true },
    title: { type: String, required: true },
    text: { type: String },
    date: { type: Date, default: Date.now, required: true },
    mail: { type: String, required: true },
    name: { type: String, required: true },
    username: { type: String, required: true },
});

const availablePostModel = mongoose.model("availableModel",availablePostSchema)
module.exports= availablePostModel;

