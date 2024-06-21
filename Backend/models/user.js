const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
      name:{type:String,required:true},
      //id:{type:String,required:true},
      picture:{type:String},
      email: { type: String, required: true },
      uniName:{ type: String, default:null }
})
const User = mongoose.model("User",UserSchema)
module.exports = User;
