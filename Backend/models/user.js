const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
      name:{type:String,required:true},
      id:{type:String,required:true},
      picture:{type:String},
      email: { type: String, required: true },
})
const User = mongoose.model("User",UserSchema)
module.exports = User;
