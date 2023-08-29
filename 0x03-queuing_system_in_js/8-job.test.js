import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";
const kue = require('kue');
const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
    before(() => queue.testMode.enter());
    afterEach(() => queue.testMode.clear());
    after(() => queue.testMode.exit());

    it('should return error if jobs is not array', () => {
        const job = {
            phoneNumber: '973254365',
            message: 'This is to test',
        };
        expect(() => createPushNotificationsJobs(job, queue)).to.throw(Error, "Jobs is not an array")
    })

    it('should create jobs when everything runs well', () => {
        const job = [
            {
            phoneNumber: '676978567',
            message: 'sdfyuyhacvjc'
        },
        {
            phoneNumber: '3253728424',
            message: 'sdgdsgdsgas'
        }]
        createPushNotificationsJobs(job, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].data).to.deep.equal({
            phoneNumber: '676978567',
            message: 'sdfyuyhacvjc'
        })
        expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3')
    })
})
