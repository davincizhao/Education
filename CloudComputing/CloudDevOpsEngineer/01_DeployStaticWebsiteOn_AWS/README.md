## Deploy Static Website on AWS
The cloud is perfect for hosting static websites that only include HTML, CSS, and JavaScript files that require no server-side processing.
The files included are: 

index.html - The Index document for the website.
/img - The background image file for the website.
/vendor - Bootssrap CSS framework, Font, and JavaScript libraries needed for the website to function.
/css - CSS files for the website.

In this project, Deploy a static website to AWS using 
- S3 
- CloudFront
- IAM

## Snapshot of project On AWS

### S3 console
![S3 console](https://github.com/davincizhao/Education/blob/main/CloudComputing/CloudDevOpsEngineer/01_DeployStaticWebsiteOn_AWS/s3_console.png)
### Config S3 AS static web hosting
![web_hosting](https://github.com/davincizhao/Education/blob/main/CloudComputing/CloudDevOpsEngineer/01_DeployStaticWebsiteOn_AWS/web_hosting.png)
### Config S3 public access
![public_access](https://github.com/davincizhao/Education/blob/main/CloudComputing/CloudDevOpsEngineer/01_DeployStaticWebsiteOn_AWS/public_access.png)
### S3 overview
![S3 overview](https://github.com/davincizhao/Education/blob/main/CloudComputing/CloudDevOpsEngineer/01_DeployStaticWebsiteOn_AWS/s3_snapshot.png)
### CDN on AWS Cloudfront 
![Cloudfront](https://github.com/davincizhao/Education/blob/main/CloudComputing/CloudDevOpsEngineer/01_DeployStaticWebsiteOn_AWS/cloudfront.png)


website address:http://deploystaticweb.s3-us-west-1.amazonaws.com/index.html


