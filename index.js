const promiseFunc = () => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve('Success!')
      }, 1)
    })
  }
  
  const callFunc = () => {
    try {
      const result = promiseFunc();
      console.log(result)
    } catch(err) {
      console.log(result)
    }
  }
  
  callFunc();