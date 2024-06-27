const User = require("../models/user")


const getUsers = async (req,res)=>{
    try {
        const users = await User.find();
        res.status(200).json(users)
     } catch(err) {
        res.status(404).json({
          
        });
     }

}


const getUsersById = async (req,res)=>{
    const userId = req.params.id
    try {
        const users = await User.findById(userId);
        res.status(200).json(users)
     } catch(err) {
        res.status(404).json({
          
        });
     }

}


const getUsersByEmail = async (req,res)=>{
    const userEmail = req.params.email
    try {
        const users = await User.findOne({email:userEmail});
        res.status(200).json(users)
     } catch(err) {
        res.status(404).json({
          
        });
     }

}

module.exports = {
    getUsers,
    getUsersById,
    getUsersByEmail,

};