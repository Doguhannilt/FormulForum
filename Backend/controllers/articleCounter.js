const User = require("../models/user")

const articleCounter= async(userId)=>{

try{
    const user = await User.findById(userId);

    if (user.articleCount == null) {
        user.articleCount = 1;
      } else {
        user.articleCount += 1;
      }
      await user.save();
  } catch (error) {
  
  }  
}

module.exports = articleCounter