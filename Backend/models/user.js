const mongoose = require("mongoose");

const UserSchema = new db.Schema({
      name:{type:String,required:true},
      picture:{type:String},
      email: { type: String, required: true },
      uniName:{type:String , default:null},
      departmentName:{type:String,default:null},
      grade:{type:Number , default:null},
      articleCount:{type:Number,default:null},    
})
const User = mongoose.model("User",UserSchema)
module.exports = User;
