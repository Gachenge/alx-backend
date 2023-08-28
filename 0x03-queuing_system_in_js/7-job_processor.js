const blacklisted = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);

    if (blacklisted.includes(phoneNumber)){
        const errorMsg = `Phone number ${phoneNumber} is blacklisted`;
        job.fail(new Error(errorMsg));
    }
    
    job.progress(50);
    console.log(`Sending notification to ${job.phoneNumber}, with message: ${job.message}`);

    job.progress(100);
    done();
}

const kue = require('kue');

const queue = kue.createQueue();

queue.process("push_notification_code_2", 2, (job, done) => {
    const { phoneNumber, message} = job.data;
    sendNotification(phoneNumber, message, job, done);
})
