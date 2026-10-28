# Week 40: Inspect where the deployment will land

Module M29 · [Course lesson](../../../site/phase-3.html#w40)

## Script

The same notebook works in development and fails in production because somebody created the job by hand with a different parameter. This week, put the deployable resources and their environment differences into reviewable configuration.

Use the Databricks CLI and bundle format supported by your workspace. The course calls these Databricks Asset Bundles. Confirm your CLI's accepted settings and supported resources before copying a complete configuration from another project.

At the root, declare the bundle identity, included resource files, variables, and targets. Define the job and pipeline resources the bundle actually supports. A target selects environment-specific settings; it should not require a separate copy of the transformation code.

Parameterize the catalog and other environment-dependent paths, and trace those values all the way into the job's reads and writes. A target called dev does not protect production if the notebook still hard-codes a production table. Think of the target as an addressed envelope: the contents still need to agree with the address on the outside.

Separate the identity that deploys resources from the identity that runs the workload. Declare the intended run-as identity using supported settings, then grant that identity only the data privileges it needs. Resource permissions and Unity Catalog data grants are related configuration concerns, but they are not interchangeable. Manage grants through supported tooling instead of inventing a resource block the schema does not recognize.

Run bundle validation before deployment. Validation checks configuration and supported references; it does not prove the pipeline's data semantics or every runtime permission. Deploy to an isolated target, inspect the resource summary, and run a smoke workflow against disposable data.

Keep deployment state associated with the correct bundle identity and target. Do not delete it to make an unexplained deployment error disappear. First inspect the CLI output, resolved settings, and workspace resources.

For your lab, record the existing inventory, the development deployment, and the difference between development and production settings. Demonstrate a controlled drift repair on a nonproduction resource, then verify both configuration and behavior.

Practical advice: treat deployment configuration as code that can send work to the wrong place. Review resolved names, paths, identities, and data targets before executing a deployment, and retain the exact commit that produced the verified resources.

## Screen example — not spoken

From the learner's completed bundle root, after configuring supported CLI authentication:

```bash
databricks version
databricks bundle validate -t dev
databricks bundle deploy -t dev
databricks bundle summary -t dev
```

Then run the declared smoke-job resource with `databricks bundle run -t dev <job-resource-key>`. Substitute an actual key from the bundle. Verify target catalog and run-as identity in the resolved configuration; no credentials belong in this script.
