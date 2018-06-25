#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'任务探测脚本，3分钟探测一次'
from model.job import Job
from service.job_service import JobService
from common.scheduler import scheduler

__author__ = 'Jiateng Liang'

config = {
    'name': '任务探测脚本',
    'cron': '{"minutes": 3}',
    'type': 1
}


def run():
    # 运行
    jobs = JobService.list_jobs_by_status(Job.Status.RUNNING.value)
    for job in jobs:
        scheduler.add_job(job)

    # 挂起
    jobs = JobService.list_jobs_by_status(Job.Status.SUSPENDED.value)
    for job in jobs:
        scheduler.suspend_job(job)

    # 停止
    jobs = JobService.list_jobs_by_status(Job.Status.STOPPED.value)
    for job in jobs:
        scheduler.remove_job(job)
