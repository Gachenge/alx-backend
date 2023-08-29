const kue = require('kue')
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error("Jobs is not an array")
    }
    jobs.forEach((job) => {
        const job1 = queue.create('push_notification_code_3', job);
        job1.on('complete', () => console.log(`Notification job ${job1.id} completed`))
        .on('failed', (error) => console.log(`Notification job ${job1.id} failed: ${error}`))
        .on('progress', (progress) => console.log(`Notification job ${job1.id} ${progress}% complete`))
        .save((err) => {
            if (!err){
                console.log(`Notification job created: ${job1.id}`)
            }
        })
    })
}

module.exports = createPushNotificationsJobs;
