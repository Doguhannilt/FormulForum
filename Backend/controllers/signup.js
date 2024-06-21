// Model
const User = require("../models/user")

// Libraries
const axios = require("axios")
const crypto = require("crypto")

// Generating unique ids
const generateUniqId =()=>{
    const bytes = crypto.randomBytes(5); 
    return bytes.toString('hex').slice(0, 10);
}

// SIGN UP
const signup = async (req,res)=>{
    try{
        const accesstoken = req.headers.authorization.split(' ')[1]
        const response = await axios.get("https://gedikkk.us.auth0.com/userinfo",{
            headers: {
                authorization: `Bearer ${accesstoken}`,
              }
        });
        const email = response.data.email;
        const account = await User.findOne({email});
        if(!account){
        // const id = generateUniqId();  
         const user = new User({
                name:response.data.name,
                picture:response.data.picture,
                email:response.data.email,
            });
            await user.save();
        }
        else{
        res.send("Hesap Mevcut");
        }
    
    }catch(error){
        res.status(404).send('Bir hata oluştu.');
    }
}

module.exports=signup
